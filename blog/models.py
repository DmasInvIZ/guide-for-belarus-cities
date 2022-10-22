from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    # author = models.CharField('Автор', max_length=200, default='')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    body = RichTextField('Пост', blank=True, null=True)  # вставка для красивого оформления поста
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
