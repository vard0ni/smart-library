from django.db import models
from datetime import date, datetime, timedelta


# сегодняшняя дата + 7 дней
def return_date_time():
	now = date.today()
	return now + timedelta(days=7)

'''
class BooksCount(models.Manager):
    def title_count(self, keyword):	
        return self.filter(title__icontains=keyword).count()
'''

class Book(models.Model):
	book_id = models.CharField('ID книги', max_length=120, null=True)
	title = models.CharField('Название книги', max_length=120, null=True)
	author = models.CharField('Автор книги', max_length=120, null=True)
	date_start = models.DateField('Дата взятия книги', default=date.today, blank=True, null=True)
	date_end = models.DateField('Дата возврата книги', default=return_date_time, blank=True, null=True)
	#book_copies = models.IntegerField()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'


class User(models.Model):
	user_id = models.CharField('ID человека', max_length=120, null=True)
	name = models.CharField('ФИО', max_length = 100, unique=True, null=True)
	position = models.CharField('Должность', default="Студент", max_length=100, null=True)
	education = models.CharField('Курс', max_length=50, null=True)
	book = models.ManyToManyField(Book, through='UserBooks', blank=True)

	def __str__(self):
   		return self.name

	class Meta:
		verbose_name = 'Человек'
		verbose_name_plural = 'Люди'

# промежуточная модель
class UserBooks(models.Model):
	book_key = models.ForeignKey('Book', on_delete=models.CASCADE)
	user_key = models.ForeignKey('User', on_delete=models.CASCADE)
	date_start = models.DateField('Дата взятия книги', default=date.today, blank=True, null=True)
	date_end = models.DateField('Дата возврата книги', default=return_date_time, blank=True, null=True)

	def __str__(self):
   		return "Book"

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'




