
from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translation

from .models import CustomBlogPost

class CustomBlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')  # Specify fields to translate

# Register the model with translation options
translation.register(CustomBlogPost, CustomBlogPostTranslationOptions)

