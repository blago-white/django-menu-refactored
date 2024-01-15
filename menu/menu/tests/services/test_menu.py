from django.test import TestCase
from django.db import models
from django.db.models.base import ObjectDoesNotExist

from menu.services import menu
from menu.models import Menu


class MenuServiceTestCase(TestCase):
    _test_service: menu.MenuService
    _test_menues: list[Menu] = None
    _test_menu: Menu = None

    def setUp(self):
        self._test_service = menu.MenuService(model=Menu)

    def test_get_all(self):
        queryset_null = self._test_service.get_all()
        self.assertFalse(queryset_null.exists())

        self._create_test_menues()

        queryset = self._test_service.get_all()
        self.assertEqual(queryset.count(), len(self._test_menues))
        self.assertEqual(queryset.first(), self._test_menues[0])

    def test_get(self):
        with self.assertRaises(ObjectDoesNotExist):
            self._test_service.get(slug="Test")

        self._create_test_menu()
        self.assertEqual(self._test_service.get(slug=self._test_menu.slug), self._test_menu)

    def test_get_childs(self):
        self.assertFalse(self._test_service.get_childs(slug="Test").exists())
        self._add_test_menu_childs()
        self.assertEqual(self._test_service.get_childs(self._test_menu.slug).count(),
                         len(self._test_menues))

    def test_get_standalone_menues(self):
        self.assertFalse(self._test_service.get_standalone_menues().exists())
        self._create_test_menues()

        standalones = self._test_service.get_standalone_menues()

        self.assertEqual(standalones.count(), len(self._test_menues))

        self.assertTrue(all(
            [menu_.parent is None for menu_ in standalones]
        ))

    def _create_test_menues(self) -> None:
        self._test_menues = [
            Menu(slug="test1", title="Test 1"),
            Menu(slug="test2", title="Test 2"),
            Menu(slug="test3", title="Test 3")
        ]

        Menu.objects.bulk_create(self._test_menues)

    def _create_test_menu(self):
        self._test_menu = Menu(slug="test_detailed", title="Test")
        self._test_menu.save()

    def _add_test_menu_childs(self):
        if not self._test_menu:
            self._create_test_menu()

        if not self._test_menues:
            self._create_test_menues()

        for menu_ in self._test_menues:
            menu_.parent = self._test_menu

        Menu.objects.bulk_update(self._test_menues, ["parent"])
