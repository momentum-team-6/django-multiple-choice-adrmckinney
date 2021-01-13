from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Snippet, Category
from .forms import AddSnippet

# Create your views here.
def index(request):
    snippets = Snippet.objects.all()
    languages = Category.objects.all()
    return render(request, 'core/index.html', {'snippets': snippets, 'languages': languages})


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