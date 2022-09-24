# Generated by Django 4.1 on 2022-09-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0005_towns'),
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/districts')),
                ('text', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'Области',
            },
        ),
    ]
