from django.contrib import admin
from django.core.mail.message import EmailMultiAlternatives
from django.urls import reverse_lazy
from django.contrib import messages

from django.utils.translation import gettext as _
from django.shortcuts import render
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from django.views import generic
from nested_inline.admin import (
    NestedModelAdmin,
    NestedTabularInline,
)


# Create your models here.


class Hr(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.CharField(max_length=900, verbose_name=_("Description"))
    slug = models.SlugField(verbose_name=_("Slug"))
    deadline = models.DateField(
        verbose_name=_("Deadline date "), auto_now_add=False, null=True, blank=True
    )
    created_at = models.DateField(verbose_name=_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Human resource")
        verbose_name_plural = _("Human resources")

    def __str__(self):
        return self.title


class ListTitle(models.Model):
    title_text = models.CharField(verbose_name=_("Text"), max_length=128, null=True)
    open_job = models.ForeignKey(
        Hr, verbose_name=_("Open job"), on_delete=models.CASCADE, null=True
    )

    class Meta:
        verbose_name = _("List title ")
        verbose_name_plural = _("List titles")

    def __str__(self):
        return u"{0}".format(self.title_text)


class ListItem(models.Model):
    item_text = RichTextField(null=True)
    list_title = models.ForeignKey(
        ListTitle, verbose_name=_("List title"), on_delete=models.CASCADE, null=True
    )

    class Meta:
        verbose_name = _("List Item ")
        verbose_name_plural = _("List Items")

    def __str__(self):
        return u"{0}".format(self.item_text)


class Questionnaire(models.Model):
    anket = models.FileField(upload_to="media/anket/", verbose_name=_("Questionnaire"))


def hrview(request):
    hr = Hr.objects.all()
    context = {"hr": hr}
    return render(request, "hr/humanresource.html", context)


class EmailForm(forms.Form):
    name = forms.CharField(max_length=100, label="Нэр")
    firstname = forms.CharField(max_length=100, label="Овог")
    attach = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}), label="CV нэмэх"
    )
    message = forms.CharField(widget=forms.Textarea, label="Нэмэлт мэдэлээлэл")


class EmailAttachementView(generic.FormView, generic.DetailView):
    model = Hr
    form_class = EmailForm
    template_name = "hr/humandetail.html"
    success_url = reverse_lazy("humandetailview")

    def get_context_data(self, **kwargs):
        context = super(EmailAttachementView, self).get_context_data(**kwargs)
        context["anket"] = Questionnaire.objects.all()
        return context

    def form_valid(self, form):
        print("valid ??")
        name = form.cleaned_data["name"]
        from_email = form.cleaned_data["firstname"]
        subject = ""
        message = form.cleaned_data["message"]
        email = "elastinex@gmail.com"
        files = self.request.FILES.getlist("attach")
        form.save()
        from django.contrib import messages

        messages.success(self.request, "Profile details updated.")
        # mail = EmailMessage(
        #     subject, from_email, message, settings.EMAIL_HOST_USER, [email]
        # )
        # for f in files:
        #     mail.attach(f.name, f.read(), f.content_type)
        # mail.send()
        subject, from_email, to = (
            "hello",
            "elastinex@gmail.com",
            "elastinex@gmail.com",
        )
        text_content = "This is an important message."
        html_content = "<p>This is an <strong>important</strong> message.</p>"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return (
            self.request,
            self.template_name,
            {
                "form": form,
                "error_message": "Hello world",
            },
        )


class InLineListItem(NestedTabularInline):
    model = ListItem
    extra = 1
    max_num = 1


class InLineListTitle(NestedTabularInline):
    model = ListTitle
    inlines = [InLineListItem]
    extra = 1


class hrAdmin(NestedModelAdmin):
    inlines = [InLineListTitle]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "description")
    search_fields = ["title"]
    list_filter = ["title"]


admin.site.register(Hr, hrAdmin)
admin.site.register(Questionnaire)
