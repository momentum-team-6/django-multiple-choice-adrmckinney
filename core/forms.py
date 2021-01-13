from  django import forms
from .models import Snippet, Category

class AddSnippet(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'title',
            'code',
            'description',
            'category',
        ]