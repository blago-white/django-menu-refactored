from django.views.generic import ListView
from django.http import HttpResponse


class MenuesListView(ListView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world!")
