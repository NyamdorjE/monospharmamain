from django import forms
from django.shortcuts import render
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _


class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Анкет"
        ordering = ['name']

    def __str__(self):
        return self.name


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["name", "phone", "email"]
        labels = {'name': "Нэр",
                  'Phone': "Утас",
                  'email': 'Имайл',
       
                  }
    
    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

def resume(request):
    if request.method == "POST":
        form - ResumeForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = ResumeForm()
    return render(request, 'hr.html', {'form': form})


admin.site.register(Resume)
