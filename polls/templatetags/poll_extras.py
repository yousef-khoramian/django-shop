from django import template

from utils.convertors import group_list

register=template.library.Library()


@register.filter()
def three_digital_currency(value:int):
    return '{:,}تومان'.format(value)


@register.filter()
def check_active(value):
    products=value.filter(is_active=True)
    return products.count()


@register.filter()
def related_product(value):
    related_product=value.filter(is_active=True).order_by('-id')[:4]
    return related_product


@register.simple_tag()
def product_categories(value,category):
    product=value.filter(category=category)[:12]
    return group_list(product,4)


@register.simple_tag(takes_context=True)
def active_url(context,*args):
    current=context.get('request').resolver_match.url_name
    if current in args :
        return 'class=active'