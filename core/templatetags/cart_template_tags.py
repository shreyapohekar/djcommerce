from django import template
from core.models import Order

register = template.Library()  # register our template tagi


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0  # if user is not authenticated return 0
