from django.db import models

from .. import models
from ..services.menu import MenuService


__all__ = ["MenuViewMixin"]


class MenuViewMixin:
    model = models.Menu
    service = MenuService
    template_name = "main.html"
