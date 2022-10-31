# Generated by Django 4.1 on 2022-10-30 19:30

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0003_usertowns_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districts',
            name='desk',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news',
            field=ckeditor.fields.RichTextField(verbose_name='Текст новости'),
        ),
        migrations.AlterField(
            model_name='towns',
            name='district',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='guide.districts', verbose_name='Область страны'),
        ),
        migrations.AlterField(
            model_name='towns',
            name='eat',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Описание мест общепита, где можно перекусить'),
        ),
        migrations.AlterField(
            model_name='towns',
            name='short_info',
            field=models.TextField(default='', max_length=2000, verbose_name='Короткое описание, для превью'),
        ),
        migrations.AlterField(
            model_name='towns',
            name='sleep',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Список и описание мет для отдыха - гостиниц, кемпингов, хостелов'),
        ),
        migrations.AlterField(
            model_name='towns',
            name='watch',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Описание достопримечательностей'),
        ),
        migrations.AlterField(
            model_name='usertowns',
            name='eat',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Описание мест общепита, где можно перекусить'),
        ),
        migrations.AlterField(
            model_name='usertowns',
            name='sleep',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Список и описание мест для отдыха - гостиниц, кемпингов, хостелов'),
        ),
        migrations.AlterField(
            model_name='usertowns',
            name='watch',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Описание достопримечательностей'),
        ),
    ]
