from django.test import TestCase

from menu.models import Menu
from menu.tests._common import MenuModelTestCaseMixin
from menu.services.menu import MenuService
from menu.templatetags.menu import draw_menu


class DrawMenuTestCase(MenuModelTestCaseMixin, TestCase):
    def test_draw_menu(self):
        self.add_test_menu_childs()

        self.assertEqual(
            draw_menu(menu_name=self.test_menu.slug),
            dict(
                object_list=MenuService(
                    model=Menu
                ).get_childs(slug=self.test_menu.slug)
            )
        )
