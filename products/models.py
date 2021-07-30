from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=180) 
   
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=180)
    description = models.TextField()
    nutrion_info = models.TextField()
    img = models.ImageField(default='fruits.jpg')
    img_url = models.URLField(max_length=1024, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
