""" product form"""
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product


class ProductForm(forms.ModelForm):
    """form for adding product to the store"""
    class Meta:
        """defines model and fields which will be used"""
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False,
        widget=CustomClearableFileInput
    )
