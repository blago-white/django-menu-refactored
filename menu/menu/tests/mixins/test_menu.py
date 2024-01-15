from django.test import TestCase

from menu.models import Menu
from menu.services.menu import MenuService
from menu.mixins.menu import MenuViewMixin, MenuItemsViewMixin
from menu.tests._common import MenuModelTestCaseMixin


class MenuViewMixinTestCase(MenuModelTestCaseMixin, TestCase):
    def test_get_queryset(self):
        self.add_test_menu_childs()

        mixin_queryset = MenuViewMixin().get_queryset()
        service_queryset = MenuViewMixin.service(model=Menu).get_standalone_menues()

        self.assertQuerysetEqual(mixin_queryset, service_queryset)


class MenuItemsViewMixinTestCase(MenuModelTestCaseMixin, TestCase):
    class TestMenuItemsViewMixin(MenuItemsViewMixin):
        slug_url_kwarg = "slug"
        model = Menu
        service = MenuService

        def __init__(self, url_slug_arg: str):
            self.kwargs = {
                self.slug_url_kwarg: url_slug_arg
            }

            super().__init__()

    def test_get_queryset(self):
        self.add_test_menu_childs()

        mixin_queryset = self.TestMenuItemsViewMixin(
            url_slug_arg=self.test_menu.slug
        ).get_queryset()
        service_queryset = self.TestMenuItemsViewMixin.service(
            model=self.TestMenuItemsViewMixin.model
        ).get_childs(
            slug=self.test_menu.slug
        )

        self.assertQuerySetEqual(mixin_queryset, service_queryset, ordered=False)
