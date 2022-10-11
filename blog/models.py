from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.conf import settings


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    author = models.CharField('Автор', max_length=200, default='')
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    body = RichTextField('Пост', blank=True, null=True)  # вставка для красивого оформления поста
    image = models.ImageField('Фотография', upload_to='static/blog', null=True, blank=True)  # надо удалить
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
