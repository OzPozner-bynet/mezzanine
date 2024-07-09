
from django.shortcuts import get_object_or_404, render
from .models import BlogPost, CustomBlogPost
from django.template.response import TemplateResponse
import logging
from custom_blog.models import CustomBlogPost
logger = logging.getLogger()


def custom_blog_post_list(
    request,
    tag=None,
    year=None,
    month=None,
    username=None,
    category=None,
    template="blog/blog_post_list.html",
    extra_context=None,
):
    """
    Display a list of blog posts that are filtered by tag, year, month,
    author or category. Custom templates are checked for using the name
    ``blog/blog_post_list_XXX.html`` where ``XXX`` is either the
    category slug or author's username if given.
    """
    templates = []
    blog_posts = CustomBlogPost.objects.published(for_user=request.user)
    if tag is not None:
        tag = get_object_or_404(Keyword, slug=tag)
        blog_posts = blog_posts.filter(keywords__keyword=tag)
    if year is not None:
        blog_posts = blog_posts.filter(publish_date__year=year)
        if month is not None:
            blog_posts = blog_posts.filter(publish_date__month=month)
            try:
                month = _(month_name[int(month)])
            except IndexError:
                raise Http404()
    if category is not None:
        category = get_object_or_404(BlogCategory, slug=category)
        blog_posts = blog_posts.filter(categories=category)
        templates.append("blog/blog_post_list_%s.html" % str(category.slug))
    author = None
    if username is not None:
        author = get_object_or_404(User, username=username)
        blog_posts = blog_posts.filter(user=author)
        templates.append("blog/blog_post_list_%s.html" % username)

    prefetch = ("categories", "keywords__keyword")
    blog_posts = blog_posts.select_related("user").prefetch_related(*prefetch)
    blog_posts = paginate(
        blog_posts,
        request.GET.get("page", 1),
        settings.BLOG_POST_PER_PAGE,
        settings.MAX_PAGING_LINKS,
    )
    context = {
        "blog_posts": blog_posts,
        "year": year,
        "month": month,
        "tag": tag,
        "category": category,
        "author": author,
    }
    context.update(extra_context or {})
    templates.append(template)
    return TemplateResponse(request, templates, context)


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
    
    logger = logging.getLogger()
    
    context = {
        "blog_post": blog_post,
        "editable_obj": blog_post,
        "related_posts": related_posts,
        'customblogpost': blog_post.first(),
        'saleskit_urls': blog_post.first().customblogpost.saleskit_urls
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