"""
import for order_number
"""
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    """
    model for orders in shop
    """
    COUNTY_CHOICES = (
        ('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Carlow', 'Carlow'),
        ('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'),
        ('Derry', 'Derry'), ('Donegal', 'Donegal'), ('Down', 'Down'),
        ('Dublin', 'Dublin'), ('Fermanagh', 'Fermanagh'), ('Galway', 'Galway'),
        ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'),
        ('Laois', 'Laois'), ('Letrim', 'Letrim'), ('Limerick', 'Limerick'),
        ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'),
        ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offlay', 'Offlay'),
        ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'), ('Tyrone', 'Tyrone'),
        ('Wateford', 'Waterford'), ('Westmeath', 'Westmeath'),
        ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow'),
    )

    order_number = models.CharField(
        max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(
        max_length=20, null=False, blank=False, default="IE")
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(
        max_length=20, null=True, blank=True, choices=COUNTY_CHOICES)
    date = models.DateTimeField()
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)  # grand-total
    orginal_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        update grand total each time a line item is added
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.discount = (settings.GUEST_DISCOUNT)
        self.delivery_cost = (settings.STANDARD_DELIVERY)
        self.total = (self.order_total + self.delivery_cost - self.discount)
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the orginal save method to set order number
        if it hasen't been set alredy.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
            self.discount = (settings.GUEST_DISCOUNT)
            self.delivery_cost = (settings.STANDARD_DELIVERY)
            self.total = (
                self.order_total + self.delivery_cost - self.discount)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    model for particular (customer) order
    """
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False, default=0)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name {self.product.name} on order {self.order.order_number}'
