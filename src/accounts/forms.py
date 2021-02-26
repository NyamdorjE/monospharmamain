from datetime import timedelta

from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class UserCacheMixin:
    user_cache = None


class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(
        label=_("Password"), strip=False, widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if settings.USE_REMEMBER_ME:
            self.fields["remember_me"] = forms.BooleanField(
                label=_("Remember me"), required=False
            )

    def clean_password(self):
        password = self.cleaned_data["password"]

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError(_("You entered an invalid password."))

        return password


class SignInViaEmailOrUsernameForm(SignIn):
    email_or_username = forms.CharField(
        label=_("Имайл & Нэр"),
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Имайл эсвэл нэр."}
        ),
    )
    password = forms.CharField(
        label=_("Нууц үг"),
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Нууц үг"}
        ),
    )

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ["email_or_username", "password", "remember_me"]
        return ["email_or_username", "password"]

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data["email_or_username"]

        user = User.objects.filter(
            Q(username=email_or_username) | Q(email__iexact=email_or_username)
        ).first()
        if not user:
            raise ValidationError(
                _("You entered an invalid email address or username.")
            )

        if not user.is_active:
            raise ValidationError(_("This account is not active."))

        self.user_cache = user

        return email_or_username


status_choices = (
    (1, _("1-р шатлалын эмнэлэг ")),
    (2, _("2-р шатлалын эмнэлэг ")),
    (3, _("3-р шатлалын эмнэлэг ")),
)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = settings.SIGN_UP_FIELDS

    username = forms.CharField(
        label=_("Овог"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    lastname = forms.CharField(
        label=_("Нэр"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    email = forms.EmailField(
        label=_("И-майл"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "   "}),
    )
    phone = forms.CharField(
        required=False,
        label=_("Утас дугаар"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    register = forms.CharField(
        required=False,
        label=_("Регистер"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    district = forms.CharField(
        required=False,
        label=_("Аймаг/дүүрэг"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    organization_name = forms.CharField(
        required=False,
        label=_("Байгууллагын нэр"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    category = forms.ChoiceField(required=False, choices=status_choices)
    license_number = forms.CharField(
        required=False,
        label=_("Лицензийн дугаар"),
        help_text=_("Заавал бөглөх шаардлаггүй"),
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
            }
        ),
    )
    password1 = forms.CharField(
        label=_("Нууц үг"),
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    password2 = forms.CharField(
        label=_("Нууц үг баталгаа"),
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": " "}),
    )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.phone = self.cleaned_data["phone"]
        user.register = self.cleaned_data["register"]
        user.district = self.cleaned_data["district"]
        user.organization_name = self.cleaned_data["organization_name"]
        user.category = self.cleaned_data["category"]
        user.license_number = self.cleaned_data["license_number"]

        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data["email"]

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_("You can not use this email address."))

        return email


status_choices = (
    (1, _("А")),
    (2, _("В")),
    (3, _("C")),
    (4, _("D")),
    (5, _("F")),
)


class PharmaSignUpView(UserCreationForm):
    class Meta:
        model = User
        fields = settings.SIGN_UP_FIELDS

    username = forms.CharField(
        label=_("Овог"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    lastname = forms.CharField(
        label=_("Нэр"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    email = forms.EmailField(
        label=_("И-майл"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "   "}),
    )
    phone = forms.CharField(
        required=False,
        label=_("Утас дугаар"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    register = forms.CharField(
        required=False,
        label=_("Регистер"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    district = forms.CharField(
        required=False,
        label=_("Аймаг/дүүрэг"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    organization_name = forms.CharField(
        required=False,
        label=_("Байгууллагын нэр"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    category = forms.ChoiceField(required=False, choices=status_choices)
    license_number = forms.CharField(
        help_text=_("Заавал бөглөх шаардлаггүй"),
        required=False,
        label=_("Лицензийн дугаар"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    password1 = forms.CharField(
        label=_("Нууц үг"),
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": " "}),
    )
    password2 = forms.CharField(
        label=_("Нууц үг баталгаа"),
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": " "}),
    )

    def save(self, commit=True):
        user = super(PharmaSignUpView, self).save(commit=False)
        user.phone = self.cleaned_data["phone"]
        user.register = self.cleaned_data["register"]
        user.district = self.cleaned_data["district"]
        user.organization_name = self.cleaned_data["organization_name"]
        user.category = self.cleaned_data["category"]
        user.license_number = self.cleaned_data["license_number"]

        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data["email"]

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_("You can not use this email address."))

        return email


class ResendActivationCodeForm(UserCacheMixin, forms.Form):
    email_or_username = forms.CharField(label=_("Email or Username"))

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data["email_or_username"]

        user = User.objects.filter(
            Q(username=email_or_username) | Q(email__iexact=email_or_username)
        ).first()
        if not user:
            raise ValidationError(
                _("You entered an invalid email address or username.")
            )

        if user.is_active:
            raise ValidationError(_("This account has already been activated."))

        activation = user.activation_set.first()
        if not activation:
            raise ValidationError(_("Activation code not found."))

        now_with_shift = timezone.now() - timedelta(hours=24)
        if activation.created_at > now_with_shift:
            raise ValidationError(
                _(
                    "Activation code has already been sent. You can request a new code in 24 hours."
                )
            )

        self.user_cache = user

        return email_or_username


class ResendActivationCodeViaEmailForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label=_("Email"))

    def clean_email(self):
        email = self.cleaned_data["email"]

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_("You entered an invalid email address."))

        if user.is_active:
            raise ValidationError(_("This account has already been activated."))

        activation = user.activation_set.first()
        if not activation:
            raise ValidationError(_("Activation code not found."))

        now_with_shift = timezone.now() - timedelta(hours=24)
        if activation.created_at > now_with_shift:
            raise ValidationError(
                _(
                    "Activation code has already been sent. You can request a new code in 24 hours."
                )
            )

        self.user_cache = user

        return email


class RestorePasswordForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label=_("Email"))

    def clean_email(self):
        email = self.cleaned_data["email"]

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_("You entered an invalid email address."))

        if not user.is_active:
            raise ValidationError(_("This account is not active."))

        self.user_cache = user

        return email


class RestorePasswordViaEmailOrUsernameForm(UserCacheMixin, forms.Form):
    email_or_username = forms.CharField(label=_("Email or Username"))

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data["email_or_username"]

        user = User.objects.filter(
            Q(username=email_or_username) | Q(email__iexact=email_or_username)
        ).first()
        if not user:
            raise ValidationError(
                _("You entered an invalid email address or username.")
            )

        if not user.is_active:
            raise ValidationError(_("This account is not active."))

        self.user_cache = user

        return email_or_username


class ChangeProfileForm(forms.Form):
    first_name = forms.CharField(label=_("First name"), max_length=30, required=False)
    last_name = forms.CharField(label=_("Last name"), max_length=150, required=False)


class ChangeEmailForm(forms.Form):
    email = forms.EmailField(label=_("Email"))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data["email"]

        if email == self.user.email:
            raise ValidationError(_("Please enter another email."))

        user = User.objects.filter(
            Q(email__iexact=email) & ~Q(id=self.user.id)
        ).exists()
        if user:
            raise ValidationError(_("You can not use this mail."))

        return email


class RemindUsernameForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label=_("Email"))

    def clean_email(self):
        email = self.cleaned_data["email"]

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_("You entered an invalid email address."))

        if not user.is_active:
            raise ValidationError(_("This account is not active."))

        self.user_cache = user

        return email
