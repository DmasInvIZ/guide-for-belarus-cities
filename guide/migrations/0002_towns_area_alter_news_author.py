# Generated by Django 4.1 on 2022-09-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='towns',
            name='area',
            field=models.CharField(choices=[('brest_district', 'Брестская область'), ('vitebsk_district', 'Витебская область'), ('gomel_district', 'Гомельская область'), ('grodno_district', 'Гродненская область'), ('minsk_district', 'Минская область'), ('mogilev_district', 'Могилевская область')], default=None, max_length=16),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(blank=True, default='Admin', max_length=20, null=True),
        ),
    ]