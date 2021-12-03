from django.db import models


class Language(models.Model):
    name = models.CharField(verbose_name="Хэлний нэр", max_length=250)
    code = models.CharField(verbose_name="Хэлний код", max_length=5)

    class Meta:
        verbose_name = "Хэл"
        verbose_name_plural = "Хэл"
        ordering = ["name"]

    def __str__(self):
        return self.name
