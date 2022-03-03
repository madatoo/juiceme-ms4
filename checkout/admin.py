"""imports"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """source CI"""
    model = OrderLineItem
    fields = ('lineitem_total', )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'date', 'delivery_cost',
        'order_total', 'total', 'orginal_bag', 'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date',
                    'full_name', 'delivery_cost',
                    'discount', 'order_total',
                    'total', 'orginal_bag', 'stripe_pid')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
