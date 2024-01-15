from django.db import models

from ..models import Menu
from .base import BaseService


class MenuService(BaseService):
    _model: Menu

    def __init__(self, model: Menu):
        self._model = model

    def get_all(self) -> models.QuerySet:
        return self._model.objects.all()

    def get(self, slug: str) -> models.Model:
        return self._model.objects.get(pk=slug)

    def get_childs(self, slug: str) -> models.QuerySet:
        return self._model.objects.filter(parent=slug)

    def get_standalone_menues(self) -> models.QuerySet:
        return self.get_all().filter(parent=None)
