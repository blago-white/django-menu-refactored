from ..services.base import BaseService
from .. import models


__all__ = ["ServiceViewMixin", "ModelListViewMixin"]


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
