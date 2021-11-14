from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    fields = ('product', 'quantity', )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    list_display =('pk', 'date', 'full_name',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)