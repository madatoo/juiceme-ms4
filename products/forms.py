""" product form"""
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """form for adding product to the store"""
    class Meta:
        """defines model and fields which will be used"""
        model = Product
        fields = '__all__'
