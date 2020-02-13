from django.shortcuts import render, get_object_or_404
from .forms import RawArticleForm
from .models import Article

from django.views.generic import (
    ListView,
    DetailView,
)

# Create your views here.

def article_create_view(request):
    article_form = RawArticleForm(request.GET)
    if request.method == "POST":
        article_form = RawArticleForm(request.POST)
        if article_form.is_valid():
            print(article_form.cleaned_data)
            Article.objects.create(**article_form.cleaned_data)
        else:
            print(article_form.errors)
    else:
        print('Error: request method is not POST')
    context = {
        'article_form': article_form,
    }
    return render(request, "articles/articles_create.html", context)

def article_detail_view(request, id):
    obj = get_object_or_404(Article, id = id)
    context = {
        'object': obj,
    }
    return render(request, 'articles/articles_detail.html', context) 

def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        'object_list' : queryset,
    }
    return render(request, 'articles/articles_list.html', context)

class ArticleClassListView(ListView):
    template_name = 'articles/articles_list.html'
    queryset = Article.objects.all()

class ArticleClassDetailView(DetailView):
    template_name = 'articles/articles_detail.html'
    queryset = Article.objects.all()

    def get_object(self, queryset=None):
        # this gets the arguemnts inside the url so <int:id>/product/<int:num>/ kwargs would have 
        # 2 arguments id and num/ we can get it like a map
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)


