from django.views.generic import ListView

from . import models, mixins


class MenuesListView(mixins.MenuViewMixin, mixins.ModelListViewMixin, mixins.MainPageViewMixin, ListView):
    pass


class MenuItemsListView(mixins.MenuItemsViewMixin, ListView):
    slug_url_kwarg = "slug"
