# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib

from django.views import generic as g
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse


class BaseMixin(object):

    def get_template_names(self):
        if self.template_name is None:
            # class name to template file name
            cname = self.__class__.__name__
            name = re.sub('(.)([A-Z][a-z]+)', r'\1%s\2' % '_', cname)
            name = re.sub('([a-z0-9])([A-Z])', r'\1%s\2' % '_', name).lower()

            namef = re.sub('(.)([A-Z][a-z]+)', r'\1%s\2' % '/', cname)
            namef = re.sub('([a-z0-9])([A-Z])', r'\1%s\2' % '/', namef).lower()

            # get app_label
            app_path = self.__module__[:-len('.views')][len('src.'):]
            app_path = app_path.replace('.', '/')

            # prepare template name
            self.template_names = ['%s/templates/%s.html' % (app_path, name), '%s/%s.html' % (
                app_path, name), '%s/templates/%s.html' % (app_path, namef), '%s/%s.html' % (app_path, namef)]
            return self.template_names

        return super(BaseMixin, self).get_template_names()


class View(BaseMixin, g.View):
    pass


class TemplateView(BaseMixin, g.TemplateView):
    pass


class FormView(BaseMixin, g.FormView):
    pass


class CreateView(BaseMixin, g.CreateView):
    pass


class UpdateView(BaseMixin, g.UpdateView):
    pass


class DeleteView(BaseMixin, g.DeleteView):
    pass


class ListView(BaseMixin, g.ListView):
    pass


class DetailView(BaseMixin, g.DetailView):
    pass


class RedirectView(g.base.RedirectView):
    pass


def error_404(request, exception):
    return render(request, '404.html', status=404)


def my_test_500_view(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponse(status=500)
