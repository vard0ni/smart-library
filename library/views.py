from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from json_views.views import JSONListView, PaginatedJSONListView
from library.models import User, Book

# Представление, которое отдаёт список каналов из urls.py

class UserListJSON(JSONListView):
    #model = User
    def get_queryset(self):
        return User.objects.get(pk=int(self.kwargs['userId']))
