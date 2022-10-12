# Generated by Django 4.1 on 2022-10-12 07:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0011_remove_towns_full_desk_towns_eat_towns_sleep_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTowns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch', ckeditor.fields.RichTextField(blank=True, default='', max_length=5000, null=True, verbose_name='Описание достопримечательностей')),
                ('eat', ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name='Описание мест общепита, где можно перекусить')),
                ('sleep', ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name='Список и описание мет для отдыха - гостиниц, кемпингов, хостелов')),
                ('district', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guide.districts')),
            ],
        ),
    ]
