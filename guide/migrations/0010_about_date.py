# Generated by Django 4.1 on 2022-10-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0009_about_alter_towns_full_desk_alter_towns_short_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]