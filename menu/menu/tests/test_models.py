from django.test import TestCase

from menu.tests._common import MenuModelTestCaseMixin
from menu.models import Menu


class MenuModelTestCase(MenuModelTestCaseMixin, TestCase):
    test_menu: Menu

    def setUp(self):
        self.create_test_menu()

    def test_get_absolute_url(self):
        self.assertEqual(
            self.test_menu.get_absolute_url(),
            f"/{self.test_menu.slug}/"
        )

    def test_str(self):
        self.assertEqual(str(self.test_menu), self.test_menu.title)
