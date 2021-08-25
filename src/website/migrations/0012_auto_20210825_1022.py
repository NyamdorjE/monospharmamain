# Generated by Django 3.1 on 2021-08-25 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20210824_2311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutuscards',
            options={'ordering': ['position'], 'verbose_name': 'Бидний тухай - Картууд', 'verbose_name_plural': 'Бидний тухай - Картууд'},
        ),
        migrations.AlterModelOptions(
            name='advice',
            options={'ordering': ['-created_on'], 'verbose_name': 'Зөвлөгөө', 'verbose_name_plural': 'Зөвлөгөө'},
        ),
        migrations.AlterModelOptions(
            name='advicecategory',
            options={'ordering': ['-title'], 'verbose_name': 'Зөвлөгөө ангиллал', 'verbose_name_plural': 'Зөвлөгөө ангиллал'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['position'], 'verbose_name': 'Нүүр хуудас - Баннер '},
        ),
        migrations.AlterModelOptions(
            name='banneraboutus',
            options={'ordering': ['position'], 'verbose_name': 'Бидний тухай - Баннер'},
        ),
        migrations.AlterModelOptions(
            name='counter',
            options={'ordering': ['number'], 'verbose_name': 'Нүүр хуудас - Тоолуур', 'verbose_name_plural': 'Нүүр хуудас - Тоолуур'},
        ),
        migrations.AlterModelOptions(
            name='directorsgreetings',
            options={'verbose_name': 'Бидний тухай - Захиралын мэндчилгээ', 'verbose_name_plural': 'Бидний тухай - Захиралын мэндчилгээ'},
        ),
        migrations.AlterModelOptions(
            name='hrbanner',
            options={'ordering': ['position'], 'verbose_name': 'Хүний нөөц - Баннер'},
        ),
        migrations.AlterModelOptions(
            name='hrcontent',
            options={'ordering': ['position'], 'verbose_name': 'Хүний нөөц - Бидэнтэй нэгдсэнээр', 'verbose_name_plural': 'Хүний нөөц - Бидэнтэй нэгдсэнээр'},
        ),
        migrations.AlterModelOptions(
            name='introduction',
            options={'verbose_name': 'Бидний тухай - Компаны танилцуулга', 'verbose_name_plural': 'Бидний тухай - Компаны танилцуулга'},
        ),
        migrations.AlterModelOptions(
            name='mission',
            options={'verbose_name': 'Бидний тухай - Эрхэм зорилго', 'verbose_name_plural': 'Бидний тухай - Эрхэм зорилго'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ['-position'], 'verbose_name': 'Бидний тухай - Хамтрагч байгуулгын зураг'},
        ),
    ]
