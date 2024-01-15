from django.db import models

from ..models import Menu
from .base import BaseService


class MenuService(BaseService):
    _model: Menu

    def __init__(self, model: Menu):
        self._model = model

    def get_all(self) -> models.QuerySet:
        return self._model.objects.all()
