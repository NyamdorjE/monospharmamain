# Generated by Django 3.2.7 on 2021-12-03 06:14

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_videonews_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_mn',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='news',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Тэкст'),
        ),
        migrations.AddField(
            model_name='news',
            name='content_mn',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Тэкст'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_mn',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Title'),
        ),
    ]
