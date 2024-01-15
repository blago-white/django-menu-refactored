from django.urls import path

from . import views


urlpatterns = [
    path("", views.MenuesListView.as_view())
]
