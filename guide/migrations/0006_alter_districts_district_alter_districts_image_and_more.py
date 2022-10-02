# Generated by Django 4.1 on 2022-10-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0005_towns_area_alter_towns_image_alter_towns_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districts',
            name='district',
            field=models.CharField(max_length=50, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='districts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/districts', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='districts',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(blank=True, default='Admin', max_length=20, null=True, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/news', verbose_name='Иллюстрация'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news',
            field=models.TextField(max_length=2000, verbose_name='Текст новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Заголовок новости'),
        ),
    ]