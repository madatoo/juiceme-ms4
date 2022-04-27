"""form for updating the default address"""
from django import forms
from .models import UserProfile


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


class UserProfileForm(forms.ModelForm):
    """form for updating the default address"""

    class Meta:
        """ all data can be updated except\
        the user and country fields """
        model = UserProfile

        fields = ['default_phone_number', 'default_street_address1',
                  'default_street_address2', 'default_town_or_city',
                  'default_postcode', 'default_county']

        default_county = forms.ChoiceField(choices=COUNTY_CHOICES)

        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """"add placeholders to the form"""
        super().__init__(*args, **kwargs)
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        self.fields['default_county'].choices = COUNTY_CHOICES
        self.fields['default_phone_number'].widget.attrs[
            'placeholder'] = 'Phone'
        self.fields['default_street_address1'].widget.attrs[
            'placeholder'] = 'Address 1'
        self.fields['default_street_address2'].widget.attrs[
            'placeholder'] = 'Address 2'
        self.fields['default_town_or_city'].widget.attrs[
            'placeholder'] = 'Town or City'
        self.fields['default_postcode'].widget.attrs[
            'placeholder'] = 'Postal Code'
        for field in self.fields:
            self.fields[field].label = False
