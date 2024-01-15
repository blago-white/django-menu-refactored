from django.db import models

from .. import models
from ..services.menu import MenuService

from . import base


__all__ = ["MenuViewMixin", "MenuItemsViewMixin"]


class MenuViewMixin(base.ServiceViewMixin):
    model = models.Menu
    service = MenuService
    _service: MenuService

    def get_queryset(self):
        return self._service.get_standalone_menues()


class MenuItemsViewMixin(MenuViewMixin, base.ServiceViewMixin):
    template_name = "menu.html"
    _service: MenuService

    def get_queryset(self):
        return self._service.get_childs(slug=self.kwargs.get(self.slug_url_kwarg))
