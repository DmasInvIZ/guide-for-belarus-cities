from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    author = models.CharField('Автор', max_length=20, default='Admin', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)  # дата публикации, обновляется при редактировании
    title = models.CharField('Заголовок новости', max_length=500)  # заголовок новости
    news = RichTextField('Текст новости', max_length=2000)  # новость
    image = models.ImageField('Иллюстрация', upload_to='static/news', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Districts(models.Model):
    name = models.CharField('Область', max_length=50)  # название области
    image = models.ImageField('Фотография', upload_to='static/districts', null=True, blank=True)
    desk = RichTextField('Описание', max_length=5000)  # описание области

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"


class Towns(models.Model):
    name = models.CharField('Город', max_length=50)  # название города
    image = models.ImageField('Фотография для превью', upload_to='static/cities', null=True, blank=True)
    short_info = models.TextField('Короткое описание, для превью', max_length=2000, default='', null=True, blank=True) \
        # короткое описание города, для страницы с общим списком городов
    watch = RichTextField('Описание достопримечательностей', max_length=5000, default='', null=True, blank=True) \
        # Что посмотреть
    eat = RichTextField('Описание мест общепита, где можно перекусить', default='', null=True, blank=True) \
        # где поесть
    sleep = RichTextField('Список и описание мет для отдыха - гостиниц, кемпингов, хостелов', default='', null=True, blank=True) \
        # где поспать
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class UserTowns(models.Model):
    pass


class About(models.Model):
    post = models.TextField('Описание страницы "О проекте"', max_length=10000, default='')
    date = models.DateTimeField(auto_now=True)  # дата публикации, обновляется при редактировании

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = "Пост 'О проекте'"
        verbose_name_plural = "Посты 'О проекте'"
