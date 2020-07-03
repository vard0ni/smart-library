from django.db import models
from datetime import date, datetime, timedelta

# Здесь пишем наши модели. Описывать таблицы в базе данных

#Foreign key links in Django models create relationships between tables.

class Channel(models.Model):    # класс Channel наследуется от класса Model
    name = models.CharField('Канал', max_length=256, primary_key=True)
    type =  models.BooleanField('Управляющий', default=False)

    def __str__(self):
        return self.name   # возвращает строковое представление нашей модели

    class Meta:   # контейнер класса с некоторыми мета-данными, преклеплённые к модели
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'

def return_date_time():
    now = date.today()
    return now + timedelta(days=7)


class Book(models.Model):
    title = models.CharField('Название книги', max_length=120)
    author = models.CharField('Автор книги', max_length=120)
    date_start = models.DateField(
    'Дата взятия книги',
     default=date.today,
     blank=True
     #input_formats=('%m/%d/%Y')
    )
    date_end = models.DateField('Дата возврата книги', default=return_date_time, blank=True)
    deadline = models.DateField('Просроченная дата возврата книги', default='', blank=True)
    #books_copies = models.CharField('Количество книг одного экземпляра', default='', max_length=50)   #экземпляры книг

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

#def studentClass(User):
    #if User.education
#    pass


class User(models.Model):
    name = models.CharField('ФИО', max_length = 100, unique=True)
    education = models.CharField('Класс', max_length=50)
    books = models.ManyToManyField(Book)  #привязка книг к одному человку
    position = models.CharField('Должность', default="Ученик", max_length=100)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
