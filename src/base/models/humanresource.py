from django.contrib import admin
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin
from django.views import generic
from django.http import HttpResponse
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from django.shortcuts import render
from django import forms
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
import re
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView
from ckeditor.fields import RichTextField
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

# Create your models here.


class Hr(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.CharField(
        max_length=900, verbose_name=_('Description'))

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


class Application(models.Model):
    firstname = models.CharField(max_length=255, verbose_name=_('Firstname'))
    lastname = models.CharField(max_length=255, verbose_name=_("Lastname"))
    phone = models.CharField(max_length=255, verbose_name=_('Phone'))

    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')

    def __str__(self):
        return self.firstname


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["firstname", "lastname", "phone", ]
        labels = {
            'firstname': "Овог",
            'lastname': "Нэр",
            'phone': "Утас",
        }

# Problem applicaion view iig Generlic.ListVIew tei hamt ajilluulj neg context-d hiih !


def application(request):
    hr = Hr.objects.all()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ApplicationForm()
    return render(request, 'hr/humanresource.html', {'form': form, 'hr': hr})


class HrList(generic.ListView):
    queryset = Hr.objects.all()
    template_name = 'hr/humanresource.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(HrList, self).get_context_data(**kwargs)
        context['hr'] = self.get_queryset()
        context['hrlist'] = Hr.objects.all()
        return context


# Register your models here.

admin.site.register(Application)


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


admin.site.register(Hr, hrAdmin)
