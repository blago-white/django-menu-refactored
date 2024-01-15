from django.test import TestCase


from menu.mixins.base import ServiceViewMixin, ModelListViewMixin
from menu.services.menu import MenuService
from menu.models import Menu
from menu.tests._common import MenuModelTestCaseMixin


class ServiceViewMixinTestCase(MenuModelTestCaseMixin, TestCase):
    class TestModelListViewMixin(ServiceViewMixin):
        service = MenuService
        model = Menu

        def get_all(self):
            return self._service.get_all()

    def test_get_service(self):
        self.create_test_menu()
        self.assertEqual(
            self.TestModelListViewMixin().get_all().first(),
            self.TestModelListViewMixin().service(model=Menu).get_all().first()
        )


class ModelListViewMixinTestCase(MenuModelTestCaseMixin, TestCase):
    test_menu: Menu = None

    class TestModelListViewMixin(ModelListViewMixin):
        model = Menu
        service = MenuService

    def test_get_queryset(self):
        self.assertEqual(
            self.TestModelListViewMixin().get_queryset().first(),
            self.TestModelListViewMixin().service(
                model=self.TestModelListViewMixin.model
            ).get_all().first()
        )
