from django.test import TestCase
from django.db import models
from django.db.models.base import ObjectDoesNotExist

from menu.services import menu
from menu.models import Menu
from .._common import MenuModelTestCaseMixin


class MenuServiceTestCase(MenuModelTestCaseMixin, TestCase):
    _test_service: menu.MenuService
    test_menues: list[Menu] = None
    test_menu: Menu = None

    def setUp(self):
        self._test_service = menu.MenuService(model=Menu)

    def test_get_all(self):
        queryset_null = self._test_service.get_all()
        self.assertFalse(queryset_null.exists())

        self.create_test_menues()

        queryset = self._test_service.get_all()

        self.assertQuerySetEqual(list(queryset), self.test_menues)

    def test_get(self):
        with self.assertRaises(ObjectDoesNotExist):
            self._test_service.get(slug="Test")

        self.create_test_menu()

        self.assertEqual(self._test_service.get(slug=self.test_menu.slug), self.test_menu)

    def test_get_childs(self):
        self.assertFalse(self._test_service.get_childs(slug="Test").exists())

        self.add_test_menu_childs()

        self.assertEqual(self._test_service.get_childs(self.test_menu.slug).count(),
                         len(self.test_menues))

    def test_get_standalone_menues(self):
        self.assertFalse(self._test_service.get_standalone_menues().exists())

        self.create_test_menues()

        standalones = self._test_service.get_standalone_menues()

        self.assertEqual(standalones.count(), len(self.test_menues))
        self.assertFalse(any(standalones.values_list("parent", flat=True)))
