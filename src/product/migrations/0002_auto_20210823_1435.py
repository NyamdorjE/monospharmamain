# Generated by Django 3.1 on 2021-08-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Нэр')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Slug')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/product/category/', verbose_name='Picture')),
                ('is_top', models.BooleanField(default=False, verbose_name='Онцлох эсэх')),
                ('is_active', models.BooleanField(default=True, verbose_name='Идэвхитэй эсэх')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
            ],
            options={
                'verbose_name': 'Бүтээгдэхүүний ангилал',
                'verbose_name_plural': 'Бүтээгдэхүүний ангилал',
                'ordering': ['created_at', 'id'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.ProductCategoryImage', verbose_name='Ангилалууд Шинэ'),
        ),
    ]
