from django.views.generic import ListView

from . import models, mixins


class MenuesListView(mixins.MenuViewMixin, mixins.ModelListViewMixin, ListView):
    pass
