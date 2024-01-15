from django import template
from django.template.loader import get_template

from ..services.menu import MenuService
from ..models import Menu


register = template.Library()
service = MenuService(model=Menu)


@register.inclusion_tag(filename=get_template("menu.html"))
def draw_menu(menu_name: str):
    return {
        'object_list': service.get_childs(slug=menu_name)
    }
