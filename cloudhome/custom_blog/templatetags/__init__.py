from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'custom_blog'

    def ready(self):
        from . import templatetags  # Import your template tags module
        templatetags.register()  # Register your tags