from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class News(models.Model):
    """Новости, на главной странице сайта"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin', verbose_name='Автор новости')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')  # дата публикации, обновляется при редактировании
    title = models.CharField('Заголовок новости', max_length=500)  # заголовок новости
    short_news = models.TextField('Короткое описание новости, превью', max_length=1000, blank=True, null=True, default='Подробности внутри')
    news = RichTextField('Текст новости')  # новость
    image = models.ImageField('Иллюстрация', upload_to='static/news', null=True, blank=True)
    slug = models.SlugField(verbose_name='URL', max_length=160, db_index=True, unique=True)  # название URL транслитом

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Districts(models.Model):
    """Области страны"""
    name = models.CharField('Область', max_length=50)  # название области
    image = models.ImageField('Фотография', upload_to='static/districts', null=True, blank=True)
    desk = RichTextField('Описание')  # описание области
    area_slug = models.SlugField(verbose_name='URL', primary_key=True, max_length=160, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"


class Towns(models.Model):
    """Города с привязкой к области"""
    name = models.CharField('Город', max_length=50)  # название города
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, default='', verbose_name='Область страны')  # название области
    image = models.ImageField('Фотография для превью', upload_to='static/cities', null=True, blank=True)
    short_info = models.TextField('Короткое описание, для превью', max_length=2000, default='',) \
        # короткое описание города, для страницы с общим списком городов
    watch = RichTextField('Описание достопримечательностей', default='') \
        # Что посмотреть
    eat = RichTextField('Описание мест общепита, где можно перекусить', default='') \
        # где поесть
    sleep = RichTextField('Список и описание мет для отдыха - гостиниц, кемпингов, хостелов', default='') \
        # где поспать
    town_slug = models.SlugField(primary_key=True, verbose_name='URL', max_length=160, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class UserTowns(models.Model):
    """Предложения публикаций от пользователей, к конкретному городу"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name='Автор публикации')
    town = models.ForeignKey(Towns, on_delete=models.CASCADE, default='', verbose_name='Город')
    is_published = models.BooleanField('В публикации', default=False)
    watch = RichTextField('Описание достопримечательностей', default='') \
        # Что посмотреть
    eat = RichTextField('Описание мест общепита, где можно перекусить', default='') \
        # где поесть
    sleep = RichTextField('Список и описание мест для отдыха - гостиниц, кемпингов, хостелов', default='') \
        # где поспать

    def __str__(self):
        return str(self.town)

    class Meta:
        verbose_name = "Публикации пользователей"
        verbose_name_plural = "Публикации пользователей"


class About(models.Model):
    """Страница 'О проекте'"""
    post = RichTextField('Описание страницы "О проекте"', default='')  # убрать количество символов
    date = models.DateTimeField(auto_now=True)  # дата публикации, обновляется при редактировании

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = "Пост 'О проекте'"
        verbose_name_plural = "Посты 'О проекте'"
