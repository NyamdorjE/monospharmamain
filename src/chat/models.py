from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from src.courses.models import Lesson
class Room(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    user = models.ManyToManyField(User, blank=True, )

class Message(models.Model):
    username = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name=_("Lesson"), on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)