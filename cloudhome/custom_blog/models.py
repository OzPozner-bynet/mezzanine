from django.db import models

# Create your models here.
from mezzanine.blog.models import BlogPost

class SalesKitURL(models.Model):
    url = models.URLField(max_length=1000)

class CustomBlogPost(BlogPost):
    saleskit_urls = models.URLField(max_length=1000,null=True)
    # saleskit_urls = models.ManyToManyField(SalesKitURL, blank=True)

class Meta:
        proxy = True
        verbose_name = "Blog Post (Custom)"
        verbose_name_plural = "Blog Posts (Custom)"
