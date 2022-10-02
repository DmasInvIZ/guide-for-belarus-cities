# Generated by Django 4.1 on 2022-10-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0004_remove_towns_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='towns',
            name='area',
            field=models.CharField(choices=[('brest_district', 'Брестская область'), ('vitebsk_district', 'Витебская область'), ('gomel_district', 'Гомельская область'), ('grodno_district', 'Гродненская область'), ('minsk_district', 'Минская область'), ('mogilev_district', 'Могилевская область')], default='', max_length=50, verbose_name='Выберите область'),
        ),
        migrations.AlterField(
            model_name='towns',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/cities', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='towns',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='towns',
            name='town',
            field=models.CharField(max_length=50, verbose_name='Город'),
        ),
    ]