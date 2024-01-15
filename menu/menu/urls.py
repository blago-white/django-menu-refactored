from django.urls import path

from . import views


urlpatterns = [
    path("", views.MenuesListView.as_view(), name="all_menues"),
    path("<str:slug>/", views.MenuItemsListView.as_view(), name="menu")
]
