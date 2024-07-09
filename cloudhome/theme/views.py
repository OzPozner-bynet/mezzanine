
from django.shortcuts import render
from .models import BlogPost, CustomBlogPost
import logging
logger = logging.getLogger()

"""
def blogpost_detail(request, slug):
    blogpost = BlogPost.objects.filter(slug=slug).prefetch_related('customblogpost')
    logger.info(f"****** inside cusom blog view.py ************\n {context}")  

    if blogpost.exists():
        context = {'blogpost': blogpost.first(), 'saleskit_urls': blogpost.first().customblogpost.saleskit_urls}
    else:
        context = {'blogpost': None}
    return render(request, '../theme/templates/blog/blog_post_detail.html', context)

"""

def my_view(request):
  keywords = request.GET.get('keywords', '')  # Get keywords from the URL parameter
  posts = CustomBlogPost.objects.filter(content__icontains=keywords)  # Filter posts based on keywords in content
  context = {'posts': posts, 'keywords': keywords}  # Pass data to the template
  logger.info(f"****** inside cusom blog view.py ************\n {context}")  
  return render(request, 'my_template.html', context)