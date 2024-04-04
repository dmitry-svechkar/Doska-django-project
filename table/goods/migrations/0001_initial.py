# Generated by Django 4.2.9 on 2024-02-11 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False, help_text='Поставьте галочку, чтобы  опубликовать.', verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('category_good_name', models.CharField(max_length=100, verbose_name='Наименование категории')),
                ('category_description', models.TextField(max_length=500, verbose_name='Описание группы товаров')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False, help_text='Поставьте галочку, чтобы  опубликовать.', verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('good_name', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='Модель товара')),
                ('condition', models.CharField(choices=[('N', 'NEW'), ('U', 'USED')], max_length=4)),
                ('in_stock', models.BooleanField(default=False)),
                ('good_cost', models.IntegerField(verbose_name='Стоимость товара')),
                ('description', models.TextField(max_length=500, verbose_name='Описание товара')),
                ('good_photo', models.ImageField(blank=True, upload_to='media/goods/', verbose_name='Изображение товара')),
                ('good_category', models.ForeignKey(on_delete=django.db.models.deletion.SET, related_name='goods', to='goods.goodcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
