from django.contrib import messages
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView,
    PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView,
    PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from django.shortcuts import get_object_or_404, redirect
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, FormView, TemplateView
from django.conf import settings
from src.quiz.models import Quiz, Category, Progress, Sitting, Question
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required, permission_required

from django.views import generic
from src.accounts.models import Profile
from .utils import (
    send_activation_email,
    send_reset_password_email,
    send_forgotten_username_email,
    send_activation_change_email,
)
from .forms import (
    SignInViaEmailOrUsernameForm,
    SignUpForm,
    RestorePasswordForm,
    RestorePasswordViaEmailOrUsernameForm,
    RemindUsernameForm,
    ResendActivationCodeForm,
    ResendActivationCodeViaEmailForm,
    ChangeProfileForm,
    ChangeEmailForm,
    PharmaSignUpView,
)
from .models import Profile, PharmaProfile


class LogInView(FormView):
    template_name = "accounts/log_in.html"

    @staticmethod
    def get_form_class(**kwargs):
        if settings.LOGIN_VIA_EMAIL_OR_USERNAME:
            return SignInViaEmailOrUsernameForm

    @method_decorator(sensitive_post_parameters("password"))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        request = self.request

        # If the test cookie worked, go ahead and delete it since its no longer needed
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()

        # The default Django's "remember me" lifetime is 2 weeks and can be changed by modifying
        # the SESSION_COOKIE_AGE settings' option.
        if settings.USE_REMEMBER_ME:
            if not form.cleaned_data["remember_me"]:
                request.session.set_expiry(0)

        login(request, form.user_cache)

        redirect_to = request.POST.get(
            REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME)
        )
        url_is_safe = is_safe_url(
            redirect_to,
            allowed_hosts=request.get_host(),
            require_https=request.is_secure(),
        )

        if url_is_safe:
            return redirect(redirect_to)

        return redirect(settings.LOGIN_REDIRECT_URL)


class SignUpView(FormView):
    template_name = "accounts/sign_up.html"
    form_class = SignUpForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)

        if settings.DISABLE_USERNAME:
            # Set a temporary username
            user.username = get_random_string()
        else:
            user.username = form.cleaned_data["username"]

        if settings.ENABLE_USER_ACTIVATION:
            user.is_active = False

        # Create a user record
        user.save()

        # Change the username to the "user_ID" form
        if settings.DISABLE_USERNAME:
            user.username = f"user_{user.id}"
            user.save()

        if settings.ENABLE_USER_ACTIVATION:

            act = Profile()
            act.user = user
            act.email = user.email
            act.phone = user.phone
            act.register = user.register
            act.district = user.district
            act.organization_name = user.organization_name
            act.category = user.category
            act.license_number = user.license_number
            act.save()

            messages.success(
                request,
                _(
                    "You are signed up. To activate the account, follow the link sent to the mail."
                ),
            )
        else:
            raw_password = form.cleaned_data["password1"]

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            messages.success(request, _("You are successfully signed up!"))

        return redirect("accounts:log_in")


class PharmaSignUpView(FormView):
    template_name = "accounts/pharmasign_up.html"
    form_class = PharmaSignUpView

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)

        if settings.DISABLE_USERNAME:
            # Set a temporary username
            user.username = get_random_string()
        else:
            user.username = form.cleaned_data["username"]

        if settings.ENABLE_USER_ACTIVATION:
            user.is_active = False

        # Create a user record
        user.save()

        # Change the username to the "user_ID" form
        if settings.DISABLE_USERNAME:
            user.username = f"user_{user.id}"
            user.save()

        if settings.ENABLE_USER_ACTIVATION:

            act = PharmaProfile()
            act.user = user
            act.email = user.email
            act.phone = user.phone
            act.register = user.register
            act.district = user.district
            act.organization_name = user.organization_name
            act.category = user.category
            act.license_number = user.license_number
            act.save()

            messages.success(
                request,
                _(
                    "You are signed up. To activate the account, follow the link sent to the mail."
                ),
            )
        else:
            raw_password = form.cleaned_data["password1"]

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            messages.success(request, _("You are successfully signed up!"))

        return redirect("accounts:log_in")


class ActivateView(View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(Profile, code=code)

        # Activate profile
        user = act.user
        user.is_active = True
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(request, _("You have successfully activated your account!"))

        return redirect("accounts:log_in")


class ResendActivationCodeView(FormView):
    template_name = "accounts/resend_activation_code.html"

    @staticmethod
    def get_form_class(**kwargs):
        if settings.DISABLE_USERNAME:
            return ResendActivationCodeViaEmailForm

        return ResendActivationCodeForm

    def form_valid(self, form):
        user = form.user_cache

        activation = user.activation_set.first()
        activation.delete()

        code = get_random_string(20)

        act = Profile()
        act.code = code
        act.user = user
        act.save()

        send_activation_email(self.request, user.email, code)

        messages.success(
            self.request,
            _("A new activation code has been sent to your email address."),
        )

        return redirect("accounts:resend_activation_code")


class RestorePasswordView(FormView):
    template_name = "accounts/restore_password.html"

    @staticmethod
    def get_form_class(**kwargs):
        if settings.RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME:
            return RestorePasswordViaEmailOrUsernameForm

        return RestorePasswordForm

    def form_valid(self, form):
        user = form.user_cache
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        if isinstance(uid, bytes):
            uid = uid.decode()

        send_reset_password_email(self.request, user.email, token, uid)

        return redirect("accounts:restore_password_done")


class ChangeProfileView(LoginRequiredMixin, FormView):
    template_name = "accounts/profile/change_profile.html"
    form_class = ChangeProfileForm

    def get_initial(self):
        user = self.request.user
        initial = super().get_initial()
        initial["first_name"] = user.first_name
        initial["last_name"] = user.last_name
        return initial

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data["first_name"]
        user.last_name = form.cleaned_data["last_name"]
        user.save()

        messages.success(self.request, _("Profile data has been successfully updated."))

        return redirect("accounts:change_profile")


class ChangeEmailView(LoginRequiredMixin, FormView):
    template_name = "accounts/profile/change_email.html"
    form_class = ChangeEmailForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial["email"] = self.request.user.email
        return initial

    def form_valid(self, form):
        user = self.request.user
        email = form.cleaned_data["email"]

        if settings.ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE:
            code = get_random_string(20)

            act = Profile()
            act.code = code
            act.user = user
            act.email = email
            act.save()

            send_activation_change_email(self.request, email, code)

            messages.success(
                self.request,
                _(
                    "To complete the change of email address, click on the link sent to it."
                ),
            )
        else:
            user.email = email
            user.save()

            messages.success(self.request, _("Email successfully changed."))

        return redirect("accounts:change_email")


class ChangeEmailActivateView(View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(Profile, code=code)

        # Change the email
        user = act.user
        user.email = act.email
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(request, _("You have successfully changed your email!"))

        return redirect("accounts:change_email")


class RemindUsernameView(FormView):
    template_name = "accounts/remind_username.html"
    form_class = RemindUsernameForm

    def form_valid(self, form):
        user = form.user_cache
        send_forgotten_username_email(user.email, user.username)

        messages.success(
            self.request, _("Your username has been successfully sent to your email.")
        )

        return redirect("accounts:remind_username")


class ChangePasswordView(BasePasswordChangeView):
    template_name = "accounts/profile/change_password.html"

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request, _("Your password was changed."))

        return redirect("accounts:change_password")


class RestorePasswordConfirmView(BasePasswordResetConfirmView):
    template_name = "accounts/restore_password_confirm.html"

    def form_valid(self, form):
        # Change the password
        form.save()

        messages.success(
            self.request,
            _("Your password has been set. You may go ahead and log in now."),
        )

        return redirect("accounts:log_in")


class RestorePasswordDoneView(BasePasswordResetDoneView):
    template_name = "accounts/restore_password_done.html"


class LogOutView(LoginRequiredMixin, BaseLogoutView):
    template_name = "accounts/log_out.html"


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        progress, c = Progress.objects.get_or_create(user=self.request.user)
        context["cat_scores"] = progress.list_all_cat_scores
        context["exams"] = progress.show_exams()
        context["user"] = User.objects.all()
        return context


class ChooseSignUpView(TemplateView):
    template_name = "accounts/choose_signup.html"