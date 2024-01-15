from .services import BaseService, MenuService
from . import models


class ServiceViewMixin:
    service: BaseService
    _service: BaseService

    def __init__(self):
        self._service = self._get_service()

    def _get_service(self):
        return self.service(model=self.model)


class ModelListViewMixin(ServiceViewMixin):
    def get_queryset(self):
        return self._service.get_all()


class MenuViewMixin:
    model = models.Menu
    service = MenuService
    template_name = "main.html"
