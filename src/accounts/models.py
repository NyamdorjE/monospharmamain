from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(_("Phone"), max_length=50)
    email = models.EmailField(blank=True)
    register = models.CharField(_("Register"), max_length=50)
    district = models.CharField(_("District"), max_length=50)
    organization_name = models.CharField(
        _("Organization name"), max_length=255)
    category = models.CharField(_("Category"), max_length=50)
    license_number = models.CharField(_("License number "), max_length=50)
