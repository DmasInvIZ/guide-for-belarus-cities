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


class Towns(models.Model):
    town = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/cities', null=True, blank=True)
    text = models.TextField(max_length=5000)

    def __str__(self):
        return self.town

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


# class City(models.Model):
#     author = models.CharField(max_length=20, default='User', null=True, blank=True)
#     date = models.DateTimeField(auto_now=True)
#     what_to_see = models.CharField(max_length=5000, blank=True)
#     where_to_eat = models.CharField(max_length=5000, blank=True)
#     where_to_sleep = models.CharField(max_length=5000, blank=True)
