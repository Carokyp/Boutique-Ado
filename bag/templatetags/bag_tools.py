from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
@register.filter(name='cal_subtotal')
def calc_subtotal(price, quantity):
    """Calculate subtotal for a line item in the bag."""
    return price * quantity