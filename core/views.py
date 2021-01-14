import json
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Snippet, Category, User
from .forms import AddSnippet, SearchForm

# Create your views here.
def index(request):
    snippets = Snippet.objects.all()
    languages = Category.objects.all()
    snippets_json = [snippet for snippet in snippets.values()]
    for snippet in snippets_json:
        user_id = snippet.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        user_name = user.username
        snippet['username'] = user_name
        category_id = snippet.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        category_name = category.language
        snippet['category'] = category_name
    print(type(snippets_json[0]))
    return render(request, 'core/index.html', {'snippets': snippets, 'languages': languages, 'snippets_json': snippets_json})


@login_required
def add_snippet(request):
    user = request.user
    if request.method == 'GET':
        form = AddSnippet()
    else:
        form = AddSnippet(data=request.POST)
        if form.is_valid():
            new_snippet = form.save(commit=False)
            new_snippet.user = request.user
            new_snippet.save()
        return redirect(to='index')

    return render(request, 'core/add_snippet.html', {'form': form, 'user': user})

def snippet_details(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    form = AddSnippet()
    return render(request, 'core/snippet_details.html', {'snippet': snippet, 'form': form})

@login_required
def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'GET':
        form = AddSnippet(instance=snippet)
    else:
        form = AddSnippet(data=request.POST, instance=snippet)
        if form.is_valid():
            form.save()
        return redirect(to='snippet_details', pk=pk)
    
    return render(request, 'core/edit_snippet.html', {'form': form, 'pk': pk})

@login_required
def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        snippet.delete()
        return redirect(to='index')
    
    return render(request, 'core/delete_snippet.html', {'snippet': snippet})

def search_results(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            search_results = Snippet.objects.filter(title_icontains=search_term)
            snippets_json = serializers.serialize('json', search_results)
            return render(request, 'core/search_results.html', {'snippets': search_results, 'snippets_json': snippets_json})
    return redirect(to='index')


