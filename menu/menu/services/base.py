from abc import ABCMeta, abstractmethod
from django.db import models


class BaseService(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, model: models.Model) -> None:
        raise NotImplemented

    @abstractmethod
    def get_all(self) -> models.QuerySet:
        raise NotImplemented

    @abstractmethod
    def get(self, *args, **kwargs) -> models.Model:
        raise NotImplemented
