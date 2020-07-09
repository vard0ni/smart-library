from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from json_views.views import JSONListView, PaginatedJSONListView, JSONDetailView
from library.models import User, Book

# Представление, которое отдаёт список каналов из urls.py

class UserDetailJSON(JSONDetailView):
	model = User
   # def get_queryset(self):
    #    return User.objects.get(pk=int(self.kwargs['pk']))

def home(request):
	return render(request, 'home/dashboard.html')

def users(request):
	return render(request, 'home/users.html')

def books(request):
	return render(request, 'home/books.html')
