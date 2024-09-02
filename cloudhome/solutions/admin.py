""" bla bla"""
from django.forms import forms, Textarea
from django.db import models
from django.contrib import admin
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField as TinyMCEField
from .models import  Solution, Vendor, Category, BusinessUnit, Product

class SolutionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TinyMCEField: {'widget': TinyMCE()},
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Solution, SolutionAdmin)
admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(BusinessUnit)
admin.site.register(Product)   