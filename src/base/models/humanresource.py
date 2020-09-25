from django.contrib import admin
from django.urls import reverse_lazy

from django.http import request
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin
from django.views import generic
from django.http import HttpResponse
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from django.shortcuts import render, redirect
from django import forms
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
import re
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView
from ckeditor.fields import RichTextField
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views import View
from django.conf import settings


# Create your models here.


class Hr(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.CharField(
        max_length=900, verbose_name=_('Description'))
    slug = models.SlugField(verbose_name=_("Slug"))
    deadline = models.DateField(verbose_name=_(
        "Deadline date "), auto_now_add=False, null=True, blank=True)
    created_at = models.DateField(verbose_name=_(
        "Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Human resource')
        verbose_name_plural = _('Human resources')

    def __str__(self):
        return self.title


class ListTitle(models.Model):
    title_text = models.CharField(
        verbose_name=_('Text'), max_length=128, null=True)
    open_job = models.ForeignKey(Hr, verbose_name=_(
        'Open job'), on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('List title ')
        verbose_name_plural = _('List titles')

    def __str__(self):
        return u'{0}'.format(self.title_text)


class ListItem(models.Model):
    item_text = RichTextField(null=True)
    list_title = models.ForeignKey(ListTitle, verbose_name=_(
        'List title'), on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('List Item ')
        verbose_name_plural = _('List Items')

    def __str__(self):
        return u'{0}'.format(self.item_text)


class Questionnaire(models.Model):
    anket = models.FileField(
        upload_to="media/anket/", verbose_name=_('Questionnaire'))

# class Application(models.Model):
#     firstname = models.CharField(max_length=255, verbose_name=_('Firstname'))
#     lastname = models.CharField(max_length=255, verbose_name=_("Lastname"))
#     phone = models.CharField(max_length=255, verbose_name=_('Phone'))

#     class Meta:
#         verbose_name = _('Application')
#         verbose_name_plural = _('Applications')

#     def __str__(self):
#         return self.firstname


# class ApplicationForm(forms.ModelForm):
#     class Meta:
#         model = Application
#         fields = ["firstname", "lastname", "phone", ]
#         labels = {
#             'firstname': "Овог",
#             'lastname': "Нэр",
#             'phone': "Утас",
#         }

# zaswar oruulj baiga


# def application(request, slug):
#     hr = get_object_or_404(Hr, slug=slug)
#     if request.method == "POST":
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             firstname = form.cleaned_data.get('firstname')
#             lastname = form.cleaned_data.get('lastname')
#             phone = form.cleaned_data.get('phone')

#             if request.user.is_authenticated():
#                 subject = str(request.user) + "'s phone"
#             else:
#                 subject = "A Visiter's comment"
#             form.save()
#         return redirect('hr/humandetail.html')
#     else:
#         form = ApplicationForm()
#     return render(request, 'hr/humandetail.html', {'form': form, 'hr': hr})


def hrview(request):
    hr = Hr.objects.all()
    file = Questionnaire.objects.all()
    context = {
        'hr': hr,
        'file': file
    }
    return render(request, 'hr/humanresource.html', context)


class EmailForm(forms.Form):
    name = forms.CharField(max_length=100, label="Нэр")
    firstname = forms.CharField(max_length=100, label="Овог")
    subject = forms.CharField(max_length=100, label="Гарчиг")
    attach = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}), label="CV нэмэх")
    message = forms.CharField(widget=forms.Textarea, label="Нэмэлт мэдэлээлэл")


class EmailAttachementView(generic.FormView):
    model = Hr
    form_class = EmailForm
    template_name = 'hr/humandetail.html'
    success_url = reverse_lazy("humandetailview")

    # def get_context_data(self, **kwargs):
    #     context = super(EmailAttachementView, self).get_context_data(**kwargs)
    #     context['form'] = self.get_form()
    #     return context
    def get_context_data(self, **kwargs):
        context = super(EmailAttachementView, self).get_context_data(**kwargs)
        print(self.kwargs)
        slug = self.kwargs.get('slug', None)
        hr = get_object_or_404(Hr, slug=slug)
        context['hr'] = hr
        return context

    # def form_valid(self, form, request):
    #     name = form.cleaned_data['name']
    #     firstname = form.cleaned_data['firstname']
    #     subject = form.cleaned_data['subject']
    #     message = form.cleaned_data['message']
    #     email = "elastinex@gmail.com"
    #     files = request.FILES.getlist('attach')
    #     mail = EmailMessage(
    #         subject, message, settings.EMAIL_HOST_USER, [email])
    #     for f in files:
    #         mail.attach(f.name, f.read(), f.content_type)
    #     mail.send()
    #     return super(EmailAttachementView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            firstname = form.cleaned_data['firstname']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = "elastinex@gmail.com"
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(
                    subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s' % email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})

# class HrList(generic.ListView):
#     queryset = Hr.objects.all()
#     template_name = 'hr/humanresource.html'
#     paginate_by = 4

#     def get_context_data(self, **kwargs):
#         context = super(HrList, self).get_context_data(**kwargs)
#         context['hr'] = self.get_queryset()
#         context['hrlist'] = Hr.objects.all()
#         return context


# class HrDetailView(generic.DetailView):
#     model = Hr
#     template_name = 'hr/humandetail.html'


# Register your models here.


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
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'description')
    search_fields = ['title']
    list_filter = ['title']


admin.site.register(Hr, hrAdmin)
admin.site.register(Questionnaire)


# class applicationAdmin(admin.ModelAdmin):
#     list_display = ('firstname', 'lastname', 'phone')
#     list_filter = ('firstname', 'lastname', 'phone')
#     search_fields = ['firstname', 'lastname', 'phone']
#     fieldsets = (
#         (None, {
#             "fields": (
#                 'firstname', 'lastname', 'phone'
#             ),
#         }),
#     )


# admin.site.register(Application, applicationAdmin)
