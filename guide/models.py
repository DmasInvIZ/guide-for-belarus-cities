from django.db import models


class News(models.Model):
    author = models.CharField(max_length=20, default='Admin', null=True, blank=True)
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
    CATEGORY_CHOICES = [
        ('brest_district', 'Брестская область'),
        ('vitebsk_district', 'Витебская область'),
        ('gomel_district', 'Гомельская область'),
        ('grodno_district', 'Гродненская область'),
        ('minsk_district', 'Минская область'),
        ('mogilev_district', 'Могилевская область'),
    ]
    area = models.CharField('Выберите область', max_length=50, choices=CATEGORY_CHOICES, default='')
    town = models.CharField('Город', max_length=50)
    image = models.ImageField('Фотография', upload_to='static/cities', null=True, blank=True)
    text = models.TextField('Описание', max_length=5000)

    def __str__(self):
        return self.town

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Districts(models.Model):
    district = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/districts', null=True, blank=True)
    text = models.TextField(max_length=5000)

    def __str__(self):
        return self.district

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"
