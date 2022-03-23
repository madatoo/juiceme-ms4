"""
This model is created for maintaining default
delivery information and order history
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(
        max_length=20, null=True, blank=True, choices=COUNTY_CHOICES)
    default_country = models.CharField(
        max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user model
    """
    if created:
        UserProfile.objects.create(user=instance)
    # if existing users - just save the profile
    instance.userprofile.save()
