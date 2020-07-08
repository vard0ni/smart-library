from django.contrib import admin
from library.models import User, Book

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'education')


admin.site.register(Book)
