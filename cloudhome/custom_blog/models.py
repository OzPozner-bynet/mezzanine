from django.db import models

# Create your models here.
from mezzanine.blog.models import BlogPost

class CustomBlogPost(BlogPost):
    saleskit_urls = models.TextField(max_length=1000,null=True)

    class Meta:
        verbose_name = "Custom Blog Post"
        verbose_name_plural = "Custom Blog Posts"
        
class Meta:
        proxy = True
        verbose_name = "Blog Post (Custom)"
        verbose_name_plural = "Blog Posts (Custom)"


"""
from django.db import models

from django.db import models
from mezzanine.core.models import Displayable

class ExtendedBlogPost(Displayable):
    post = models.ForeignKey("blog.BlogPost", on_delete=models.CASCADE)
    urls = models.TextField(blank=True, help_text="Enter URLs separated by commas (,)")

    class Meta:
        verbose_name = "Extended Blog Post"
        verbose_name_plural = "Extended Blog Posts"

    def __str__(self):
        return self.post.title


# Create your models here.
from mezzanine.blog.models import BlogPost

class SalesKitURL(models.Model):
    #url = models.URLField(max_length=1000,null=True)
    url = models.CharField(max_length=200)

class CustomBlogPost(BlogPost):
    #saleskit_urls = models.URLField(max_length=1000,null=True)
    # saleskit_urls = models.ManyToManyField(SalesKitURL, blank=True)
    saleskit_url = models.OneToOneField(SalesKitURL, blank=True, on_delete=models.CASCADE)

class Meta:
        proxy = True
        verbose_name = "Blog Post (Custom)"
        verbose_name_plural = "Blog Posts (Custom)"
"""