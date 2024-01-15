from menu.models import Menu


class MenuModelTestCaseMixin:
    test_menu: Menu = None
    test_menues: list[Menu] = None

    def create_test_menues(self) -> None:
        self.test_menues = [
            Menu(slug="test1", title="Test 1"),
            Menu(slug="test2", title="Test 2"),
            Menu(slug="test3", title="Test 3")
        ]

        Menu.objects.bulk_create(self.test_menues)

    def create_test_menu(self):
        self.test_menu = Menu(slug="test_detailed", title="Test")
        self.test_menu.save()

    def add_test_menu_childs(self):
        if not self.test_menu:
            self.create_test_menu()

        if not self.test_menues:
            self.create_test_menues()

        for menu_ in self.test_menues:
            menu_.parent = self.test_menu

        Menu.objects.bulk_update(self.test_menues, ["parent"])
