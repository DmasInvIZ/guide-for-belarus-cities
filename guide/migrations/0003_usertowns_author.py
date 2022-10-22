# Generated by Django 4.1 on 2022-10-22 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guide', '0002_alter_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertowns',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор публикации'),
        ),
    ]
