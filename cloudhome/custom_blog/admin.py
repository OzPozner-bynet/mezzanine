from django.contrib import admin

# Register your models here.
from django import forms
from .models import BlogPost
from mezzanine.blog.admin import BlogPostAdmin
from .models import CustomBlogPost, SalesKitURL
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # Import CKEditor widget


class CustomBlogPostAdminForm(forms.ModelForm):
    saleskit_urls = forms.CharField(widget=CKEditorUploadingWidget())  # Use CKEditor widget for SalesKitURLS

    class Meta:
        model = CustomBlogPost
        fields = '__all__'

class CustomBlogPostAdmin(BlogPostAdmin):
    form = CustomBlogPostAdminForm

def has_module_permission(self, request):
        # Override permission check to allow Bynet group, staff, and admin
        return request.user.is_staff or request.user.is_superuser or request.user.groups.filter(name='Bynet').exists()

def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not (request.user.is_staff or request.user.is_superuser or request.user.groups.filter(name='Bynet').exists()):
            del form.fields['saleskit_urls']  # Hide field if not authorized
        return form

#admin.site.unregister(BlogPost)
admin.site.register(CustomBlogPost, CustomBlogPostAdmin)
