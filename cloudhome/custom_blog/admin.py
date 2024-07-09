from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost 
from .models import CustomBlogPost
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # Import CKEditor widget

class CustomBlogPostAdminForm(forms.ModelForm):
    saleskit_url = forms.CharField(widget=CKEditorUploadingWidget())  # Use CKEditor widget for SalesKitURLS

    class Meta:
        model = CustomBlogPost
        fields = '__all__'



class CustomBlogPostAdmin(BlogPostAdmin):
    fieldsets = list(BlogPostAdmin.fieldsets) + [
        ("Extra", {
            "fields": ["saleskit_urls"]
        }),
    ]
#admin.site.unregister(BlogPost)
admin.site.register(CustomBlogPost, CustomBlogPostAdmin)

 