from django.db import models
from datetime import date, datetime, timedelta


def return_date_time():
    now = date.today()
    return now + timedelta(days=7)


class Book(models.Model):
    title = models.CharField('Название книги', max_length=120, null=True)
    author = models.CharField('Автор книги', max_length=120, null=True)
    date_start = models.DateField('Дата взятия книги', default=date.today, null=True)
    date_end = models.DateField('Дата возврата книги', default=return_date_time, blank=True, null=True)
    deadline = models.DateField('Просроченная дата возврата книги', blank=True, null=True)
    #book_copies = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class User(models.Model):
    name = models.CharField('ФИО', max_length = 100, unique=True)
    education = models.CharField('Класс', max_length=50)
    books = models.ManyToManyField(Book, blank=True)
    position = models.CharField('Должность', default="Ученик", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
