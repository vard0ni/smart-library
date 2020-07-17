from django.contrib import admin
from library.models import *

# отображение информации о книгах в моделе пользователя
class BooksInline(admin.TabularInline):
	model = UserBooks


class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'position', 'education')
	inlines = [BooksInline,]
	exclude = ('book',)


class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date_start', 'date_end')
	

admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)