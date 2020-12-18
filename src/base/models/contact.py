from django import forms
from django.shortcuts import render
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default="")
    Phone = models.CharField(max_length=10, default="")
    message = models.TextField()

    class Meta:
        verbose_name = "Холбоо барих"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "Phone", "email", "message"]
        labels = {
            "name": "Нэр",
            "Phone": "Утас",
            "email": "Имайл",
            "message": "Холбоо барих",
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
        self.helper.form_method = "POST"


def contact(contact):
    if contact.method == "POST":
        form = ContactForm(contact.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(contact, "Амжилттай илгээгдлээ")
    else:
        form = ContactForm()
    return render(contact, "homecontact.html", {"form": form})


admin.site.register(Contact)
