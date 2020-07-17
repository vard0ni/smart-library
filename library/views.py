from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from json_views.views import JSONDetailView, JSONListView, PaginatedJSONListView
from library.models import *


# возврат json пользователя по url 
class UserDetailJSON(JSONDetailView):
	#model = User
    def get_queryset(self):
        return User.objects.filter(pk=int(self.kwargs['pk'])).values('id', 'name', 'position', 'education')


# возврат json книг по url 
class BookDetailJSON(JSONListView):
	def get_queryset(self):
		return User.objects.filter(pk=self.kwargs['pk']).values('book__title', 'book__author','book__date_start', 'book__date_end', 'book__id')
	
# рендер главной страницы приложения	
def home(request):
	return render(request, 'home/index.html')


