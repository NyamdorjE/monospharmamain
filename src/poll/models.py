from django.db import models
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    position = models.IntegerField(verbose_name=_('Position'))
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    class Meta:
        verbose_name = _("Санал асуулга")
        verbose_name_plural = _("Санал асуулга")


class Question(models.Model):
    question = models.TextField()
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name="poll", null=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_corret = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
