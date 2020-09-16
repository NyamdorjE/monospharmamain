from django.core.mail import send_mail
from django import forms
from django.shortcuts import render
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMessage
from django.views import View
from django.conf import settings


# class EmailForm(forms.Form):
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=100)
#     attach = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     message = forms.CharField(widget=forms.Textarea)


# class EmailAttachementView(View):
#     form_class = EmailForm
#     template_name = 'emailattachment.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'email_form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)

#         if form.is_valid():

#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             email = form.cleaned_data['email']
#             files = request.FILES.getlist('attach')

#             try:
#                 mail = EmailMessage(
#                     subject, message, settings.EMAIL_HOST_USER, [email])
#                 for f in files:
#                     mail.attach(f.name, f.read(), f.content_type)
#                 mail.send()
#                 return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s' % email})
#             except:
#                 return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

#         return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})
