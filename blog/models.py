from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse  # Новый импорт

from core import settings


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    author = models.CharField('Автор', max_length=200, default='')
    body = models.TextField('Пост')
    image = models.ImageField('Фотография', upload_to='static/news', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
