
from django.shortcuts import get_object_or_404, render
from .models import BlogPost, CustomBlogPost
from django.template.response import TemplateResponse
import logging
from custom_blog.models import CustomBlogPost
logger = logging.getLogger()


def custom_blog_post_detail(
    request,
    slug,
    year=None,
    month=None,
    day=None,
    template="blog/blog_post_detail.html",
    extra_context=None,
):
    """. Custom templates are checked for using the name
    ``blog/blog_post_detail_XXX.html`` where ``XXX`` is the blog
    posts's slug.
    """
    
   
    #blog_posts = BlogPost.objects.published(for_user=request.user).select_related()
    blog_posts = CustomBlogPost.objects.published(for_user=request.user).select_related()
    blog_post = get_object_or_404(blog_posts, slug=slug)
    related_posts = blog_post.related_posts.published(for_user=request.user)
    # blogpost = BlogPost.objects.filter(slug=slug).prefetch_related('customblogpost')
    import logging
    logger = logging.getLogger()
    
    context = {
        "blog_post": blog_post,
        "editable_obj": blog_post,
        "related_posts": related_posts,
    #    'customblogpost': blogpost.first(), 'saleskit_urls': blogpost.first().customblogpost.saleskit_urls
    }
    logger.info(f"****** inside cusom blog view.py ************\n {context}") 
    context.update(extra_context or {})
    templates = ["blog/blog_post_detail_%s.html" % str(slug), template]
    return TemplateResponse(request, templates, context)


def my_view(request):
  keywords = request.GET.get('keywords', '')  # Get keywords from the URL parameter
  posts = CustomBlogPost.objects.filter(content__icontains=keywords)  # Filter posts based on keywords in content
  context = {'posts': posts, 'keywords': keywords}  # Pass data to the template
  return render(request, 'my_template.html', context)



"""
def blogpost_detail(request, slug):
    blogpost = BlogPost.objects.filter(slug=slug).prefetch_related('customblogpost')
    logger.info(f"****** inside cusom blog view.py ************\n {context}")  

    if blogpost.exists():
        context = {'blogpost': blogpost.first(), 'saleskit_urls': blogpost.first().customblogpost.saleskit_urls}
    else:
        context = {'blogpost': None}
    return render(request, '../theme/templates/blog/blog_post_detail.html', context)




from django.shortcuts import render
from .models import BlogPost, CustomBlogPost
import logging
logger = logging.getLogger()

def blogpost_detail(request, slug):
    blogpost = BlogPost.objects.filter(slug=slug).prefetch_related('customblogpost')
    logger.info(f"****** inside cusom blog view.py ************\n {context}")  

    if blogpost.exists():
        context = {'blogpost': blogpost.first(), 'saleskit_urls': blogpost.first().customblogpost.saleskit_urls}
    else:
        context = {'blogpost': None}
    return render(request, 'blogpost_detail.html', context)







from django.shortcuts import render
from .models import CustomBlogPost
import logging
logger = logging.getLogger()

def custom_blog_detail(request, slug):
    post = CustomBlogPost.objects.get(slug=slug)  # Fetch the post
    context = {'post': post}  # Add the post object to context
    logger.info(f"****** inside cusom blog view.py ************\n {context}")  
    return render(request, 'blog_POST_detail.html', context)

from django.shortcuts import render
from .models import CustomBlogPost
from rest_framework import serializers
# Create your views here.

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomBlogPost
        fields = '__all__'  # Include all fields (adjust as needed)


post_serializer = BlogPostSerializer(post)
serialized_data = post_serializer.data

context = {'post': post, 'serialized_post': serialized_data}
print(context)
return render(request, 'blog_post_detail.html', context)
"""