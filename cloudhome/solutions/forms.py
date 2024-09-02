from django import forms
from tinymce.widgets import TinyMCE
from .models import Solution

class SolutionForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE())
    usp = forms.CharField(widget=TinyMCE())
    target_personas = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Solution
        fields = '__all__'