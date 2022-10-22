from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# публикация отзывов о путешествиях
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    author = models.ForeignKey(User, default='Удаленный пользователь', on_delete=models.SET_DEFAULT, verbose_name='Автор поста')
    body = RichTextField('Пост', blank=True, null=True)  # вставка для красивого оформления поста
    date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
