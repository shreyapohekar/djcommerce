from django.contrib import admin

# Register your models here.
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False,
                    refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


# it displays all the specified field as the part of the list so that its easy to manage
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'billing_address',
                    'shipping_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'billing_address',
        'shipping_address',
        'payment',
        'coupon'
    ]
    search_fields = [
        'user__username',  # this is a form for searching the field not the object (ie user)
        'ref_code'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]

    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)  # OrderAdmin creates a tabular view of all the fields so that there is no
# need to click  every order to view its important details
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
