from django.shortcuts import render
from .models import TextSearch
from .forms import TextForm
from django.shortcuts import redirect
from .search import Search

def search_list(request):
    text = TextSearch.objects.all()
    return render(request, 'tapsearch/search_list.html', {'text':text[:2]})

def text_new(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.save(commit=False)
            text.save()
            t = text.text
            w = text.word
            s = Search(t, w)
            ans = s.search()
            return render(request, 'tapsearch/ans.html', {'ans':ans})
    else:
        form = TextForm()
    return render(request, 'tapsearch/post_text.html', {'form':form})