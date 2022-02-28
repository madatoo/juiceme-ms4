from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    fields = ('lineitem_total', )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    list_display =('order_number', 'date', 'full_name', 'delivery_cost', 'discount', 'order_total', 'total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)