from django.db import models


class News(models.Model):
    author = models.CharField('Автор', max_length=20, default='Admin', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)                                         # дата публикации, обновляется при редактировании
    title = models.CharField('Заголовок новости', max_length=500)                      # заголовок новости
    news = models.TextField('Текст новости', max_length=2000)                          # новость
    image = models.ImageField('Иллюстрация', upload_to='static/news', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Districts(models.Model):
    name = models.CharField('Область', max_length=50)                               # название области
    image = models.ImageField('Фотография', upload_to='static/districts', null=True, blank=True)
    desk = models.TextField('Описание', max_length=5000)                            # описание области

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"


class Towns(models.Model):
    name = models.CharField('Город', max_length=50)                                 # название города
    image = models.ImageField('Фотография', upload_to='static/cities', null=True, blank=True)
    short_info = models.TextField('Короткое описание', max_length=2000, default='') # короткое описание города, для страницы с общим списком городов   ИЗМЕНИТЬ!!
    full_desk = models.TextField('Полное описание', max_length=5000, default='')    # Полное описание города, для страницы с детальной информацией   ИЗМЕНИТЬ!!
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
