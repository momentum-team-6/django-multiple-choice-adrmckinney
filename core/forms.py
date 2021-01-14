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

class SearchForm(forms.Form):
    search_term = forms.CharField(label='search', max_length=50)