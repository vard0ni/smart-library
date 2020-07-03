from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from json_views.views import JSONListView, PaginatedJSONListView
from library.models import User, Book, Channel


def index(request):
    return HttpResponse('Hello, World!')

'''
class ChannelListJSON(JSONListView):
    model = Channel # отправляются в бд и выбирают объекты модели Channel

class BookListView(View):
    def get(self, request, *args, **kwargs):
		books = Book.objects.all()
		context = {'books': books}
		return render(request, "../templates/book-list.html", context=context)
    def post(self, request):
'''
