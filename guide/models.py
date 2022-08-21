from django.db import models


class News(models.Model):
    author = models.CharField(max_length=20, default='User', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=500)
    news = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='static/news', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
