# Generated by Django 4.1 on 2022-10-12 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guide', '0012_usertowns'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertowns',
            options={'verbose_name': 'Публикации пользователей', 'verbose_name_plural': 'Публикации пользователей'},
        ),
        migrations.AddField(
            model_name='usertowns',
            name='is_published',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='usertowns',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
