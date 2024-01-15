from django.test import TestCase

from menu.models import Menu


class MenuModelTestCase(TestCase):
    _test_menu: Menu

    def setUp(self):
        self._test_menu = Menu(slug="test", title="Test")
        self._test_menu.save()

    def test_get_absolute_url(self):
        self.assertEqual(
            self._test_menu.get_absolute_url(),
            f"/{self._test_menu.slug}/"
        )

    def test_str(self):
        self.assertEqual(str(self._test_menu), self._test_menu.title)
