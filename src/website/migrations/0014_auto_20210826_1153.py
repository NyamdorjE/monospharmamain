# Generated by Django 3.1 on 2021-08-26 03:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20210825_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=550, null=True, verbose_name='Гарчиг'),
        ),
    ]
