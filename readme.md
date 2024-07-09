Install venv
activate venv


pip install mezzanine
pip install django-modeltranslation
pip install django-ckeditor
pip install --upgrade cuser
pip install --upgrade modeltranslation



fixes

add to .venv\Lib\site-packages\django\template\defaulttags.py
```
@register.filter
def url_by_pipe(value):
  """Splits a string by pipe ("|") and returns a string.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  try:
    url=value.split("|")[0]
  except:
    url=value    
  return value.split("|")[0]

@register.filter
def title_by_pipe(value):
  """Splits a string by pipe ("|") and returns a string.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  try:
    title = value.split("|")[1]
  except:
    title = value
  return title

@register.filter
def split_by_double_pipe(value):
  """Splits a string by pipe ("|") and returns a list.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  return value.split("||")

@register.filter
def split_by_pipe(value):
  """Splits a string by pipe ("|") and returns a list.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  return value.split("||")
```



change .venv\Lib\site-packages\mezzanine\blog\views.py
to
```

def blog_post_detail(
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
    
    from custom_blog.models import CustomBlogPost
    #blog_posts = BlogPost.objects.published(for_user=request.user).select_related()
    blog_posts = CustomBlogPost.objects.published(for_user=request.user).select_related()
    blog_post = get_object_or_404(blog_posts, slug=slug)
    related_posts = blog_post.related_posts.published(for_user=request.user)
  
    context = {
        "blog_post": blog_post,
        "editable_obj": blog_post,
        "related_posts": related_posts,
  
    }
    context.update(extra_context or {})
    templates = ["blog/blog_post_detail_%s.html" % str(slug), template]
    return TemplateResponse(request, templates, context)

```

change .venv\Lib\site-packages\mezzanine\utils\html.py on line 113
```
#protocols=ALLOWED_PROTOCOLS + ["tel"],
        protocols = ALLOWED_PROTOCOLS.union(set(["tel"])),
```


to run
python manage.py runserver 0.0.0.0:80

to migrate 

python manage.py makemigrations
python manage.py migrate