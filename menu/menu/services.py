from abc import ABC, abstractmethod

from django.db import models
from .models import Menu


class BaseService(ABC):
    @abstractmethod
    def __init__(self, model: models.Model) -> None:
        raise NotImplemented

    @abstractmethod
    def get_all(self) -> models.QuerySet:
        raise NotImplemented


class MenuService(BaseService):
    _model: Menu

    def __init__(self, model: Menu):
        self._model = model

    def get_all(self) -> models.QuerySet:
        return self._model.objects.all()
