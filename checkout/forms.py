"""form for completing the order"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """set IE as required field by stripe"""
    country = forms.CharField(disabled=True, initial='IE')

    class Meta:
        """defined fields"""
        model = Order

        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'county',
            'country'
        )

    def __init__(self, *args, **kwargs):
        """"add placeholders to the form"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone',
            'street_address1': 'Address 1',
            'street_address2': 'Address 2',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
            'county': 'County',
            'country': 'Country'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
