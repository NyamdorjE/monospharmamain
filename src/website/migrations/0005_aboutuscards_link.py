# Generated by Django 3.1 on 2021-08-24 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_hrbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuscards',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Үсрэх линк'),
        ),
    ]
