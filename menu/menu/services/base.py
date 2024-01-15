from abc import ABC, abstractmethod
from django.db import models


class BaseService(ABC):
    @abstractmethod
    def __init__(self, model: models.Model) -> None:
        raise NotImplemented

    @abstractmethod
    def get_all(self) -> models.QuerySet:
        raise NotImplemented
