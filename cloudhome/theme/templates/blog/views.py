
from django.shortcuts import render
from django.db import models
from models import CustomBlogPost

def custom_blog_detail(request, slug):
    post = CustomBlogPost.objects.get(slug=slug)  # Fetch the post
    context = {'post': post}  # Add the post object to context
    print(context) 
    return render(request, 'blog_POST_detail.html', context)

"""
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