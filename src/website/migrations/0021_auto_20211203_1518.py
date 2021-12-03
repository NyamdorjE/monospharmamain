# Generated by Django 3.2.7 on 2021-12-03 07:18

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20211203_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuscards',
            name='context_mn',
            field=models.TextField(null=True, verbose_name='Контэнт'),
        ),
        migrations.AddField(
            model_name='aboutuscards',
            name='title_mn',
            field=models.CharField(max_length=500, null=True, verbose_name='Гарчиг'),
        ),
        migrations.AddField(
            model_name='advice',
            name='content_mn',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='advice',
            name='title_mn',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='advicecategory',
            name='title_mn',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='banner',
            name='content_mn',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='banner',
            name='link_text_mn',
            field=models.CharField(max_length=550, null=True, verbose_name='Линк орох тэкст'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_mn',
            field=models.CharField(max_length=550, null=True, verbose_name='Гарчиг'),
        ),
        migrations.AddField(
            model_name='banneraboutus',
            name='content_mn',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='banneraboutus',
            name='link_text_mn',
            field=models.CharField(blank=True, max_length=550, null=True, verbose_name='Линк орох тэкст'),
        ),
        migrations.AddField(
            model_name='banneraboutus',
            name='title_mn',
            field=models.CharField(blank=True, max_length=550, null=True, verbose_name='Гарчиг'),
        ),
        migrations.AddField(
            model_name='directorsgreetings',
            name='context_mn',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Контэнт'),
        ),
        migrations.AddField(
            model_name='hrbanner',
            name='content_mn',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='hrbanner',
            name='link_text_mn',
            field=models.CharField(blank=True, max_length=550, null=True, verbose_name='Линк орох тэкст'),
        ),
        migrations.AddField(
            model_name='hrbanner',
            name='title_mn',
            field=models.CharField(blank=True, max_length=550, null=True, verbose_name='Гарчиг'),
        ),
        migrations.AddField(
            model_name='hrcard',
            name='title_mn',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Гарчиг'),
        ),
        migrations.AddField(
            model_name='hrcontent',
            name='content_mn',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='hrcontent',
            name='title_mn',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Гарчиг'),
        ),
        migrations.AddField(
            model_name='introduction',
            name='context_mn',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Танилцуулга'),
        ),
        migrations.AddField(
            model_name='mission',
            name='context_mn',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Эрхэм зорилго'),
        ),
        migrations.AddField(
            model_name='taniltsuulga',
            name='content_mn',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='taniltsuulga',
            name='title_mn',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Гарчиг'),
        ),
        migrations.AddField(
            model_name='testimonail',
            name='content_mn',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='testimonail',
            name='job_mn',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Guest job'),
        ),
        migrations.AddField(
            model_name='testimonail',
            name='person_mn',
            field=models.CharField(max_length=55, null=True, verbose_name='Guest'),
        ),
        migrations.AddField(
            model_name='testimonail',
            name='profile_mn',
            field=models.FileField(null=True, upload_to='media/testimonails/profile'),
        ),
    ]
