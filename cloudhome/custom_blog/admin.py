from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
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
            "fields": ["saleskit_urls","direction"]
        }),
    ]

admin.site.register(CustomBlogPost, CustomBlogPostAdmin)



"""
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from .models import ExtendedBlogPost


class CustomBlogPostAdmin(BlogPostAdmin):
    fieldsets = list(BlogPostAdmin.fieldsets) + [
        ("Extra Fields", {
            "fields": ["urls"],
        }),
    ]

admin.site.register(ExtendedBlogPost, CustomBlogPostAdmin)


from django.contrib import admin
from .models import ExtendedBlogPost

class ExtendedBlogPostAdmin(admin.StackedInline):
    model = ExtendedBlogPost
    inlines = []
    fk_name = 'post'

    def get_formsets(self, request, obj=None):
        # Access the urls field through the model instance
        if obj:
            formsets = super().get_formsets(request, obj)
            for formset in formsets:
                formset.form.base_fields['urls'].initial = obj.urls.split(",")
            return formsets
        return super().get_formsets(request, obj)


admin.site.register(ExtendedBlogPost, ExtendedBlogPostAdmin)



""
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from .models import CustomBlogPost, SalesKitURL
from django import forms
from django.db import models

class SingleLineWidget(forms.TextInput):
    # Optional CSS class to style the input field for single line display
    attrs = {'class': 'single-line-input'}

class MyModel(models.Model):
    single_line_text = models.TextField()

    def __str__(self):
        return self.single_line_text

class MyModelForm(forms.ModelForm):
    class Meta:
        model = SalesKitURL
        fields = '__all__'

    single_line_text = forms.CharField(widget=SingleLineWidget)  # Override widget for single line display

class CustomBlogPostAdmin(BlogPostAdmin):
    fieldsets = list(BlogPostAdmin.fieldsets) + [
        ("Sales KIt URL", {
            "fields": ["saleskit_url"],
        }),
    ]

admin.site.register(CustomBlogPost, CustomBlogPostAdmin)


from django.contrib import admin

# Register your models here.
from django import forms
from .models import BlogPost
from mezzanine.blog.admin import BlogPostAdmin
from .models import CustomBlogPost, SalesKitURL
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # Import CKEditor widget


class BlogPostDetailsInline(admin.StackedInline):# Or TabularInline

    model = SalesKitURL
    extra = 0# Set to 0 to prevent creating multiple details objects by default

class BlogPostExtendedAdmin(admin.ModelAdmin):
    inlines = [BlogPostDetailsInline]

class BlogPostExtendedForm(forms.ModelForm):
    class Meta:
        model = CustomBlogPost
        fields = ['title', 'content', 'saleskit_url']  # Include the 'details' field

class CustomBlogPostAdminForm(forms.ModelForm):
    saleskit_url = forms.CharField(widget=CKEditorUploadingWidget())  # Use CKEditor widget for SalesKitURLS

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
#admin.site.register(CustomBlogPost, CustomBlogPostAdmin)
admin.site.register(CustomBlogPost, BlogPostExtendedAdmin)
"""