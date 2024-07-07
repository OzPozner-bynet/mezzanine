from django.db import models
"""
from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translation
"""
# Create your models here.
from mezzanine.blog.models import BlogPost

class CustomBlogPost(BlogPost):
    # blog_post = models.OneToOneField(BlogPost, on_delete=models.CASCADE, related_name='customblogpost')  # Specify related_name
    blogpost_ptr = models.OneToOneField(BlogPost, on_delete=models.CASCADE, parent_link=True)  # Likely for concrete model inheritance

    saleskit_urls = models.TextField(max_length=1000,null=True)
    direction = models.TextField(max_length=3,null=False,default="RTL")

    class Meta:
        verbose_name = "Custom Blog Post"
        verbose_name_plural = "Custom Blog Posts"
        
class Meta:
        proxy = True
        verbose_name = "Blog Post (Custom)"
        verbose_name_plural = "Blog Posts (Custom)"