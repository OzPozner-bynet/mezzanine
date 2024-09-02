"""
# Models for Business Unit, Vendor, and Product (assuming they exist)
# ... (replace with your models)
"""
from django.db import models
from django.utils.text import Truncator
from tinymce.models import HTMLField as TinyMCEField
from mezzanine.core.models import Displayable


# Models for Business Unit, Vendor, and Product (assuming they exist)
# ... (replace with your models)

from django.urls import reverse

class Solution(Displayable):

    
    category = models.ForeignKey('solutions.Category', on_delete=models.CASCADE)  # Replace Category model
    title = models.CharField(max_length=50)
    business_unit = models.ForeignKey('solutions.BusinessUnit', on_delete=models.CASCADE)  # Replace BusinessUnit model
    vendors = models.ManyToManyField('solutions.Vendor', blank=True)  # Replace Vendor model
    products = models.ManyToManyField('solutions.Product', blank=True)  # Replace Product model
    description = TinyMCEField()
    usp = TinyMCEField()
    target_personas = TinyMCEField()

    def get_absolute_url(self):
        return reverse('solution_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Solution"
        verbose_name_plural = "Solutions"

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class BusinessUnit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_information = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() 


    def __str__(self):
        return self.name
