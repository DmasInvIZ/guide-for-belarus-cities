# Generated by Django 4.1 on 2022-08-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0003_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
