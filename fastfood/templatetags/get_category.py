from django import template

register = template.Library()


@register.simple_tag
def get_category(food):
    return food.category.name