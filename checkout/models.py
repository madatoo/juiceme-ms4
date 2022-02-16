"""
import for order_number
"""
import uuid

from django.db import models
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
        max_length=20, null=False, blank=False, default="Ireland")
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(
        max_length=20, null=True, blank=True, choices=COUNTY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the orginal save method to set order number
        if it hasen't been set alredy.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    model for particular (customer) order
    """
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f'Name {self.product.name} on order {self.order.order_number}'
