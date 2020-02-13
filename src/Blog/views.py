from django.shortcuts import render, get_object_or_404
from .forms import ArticleModelForm
from .models import Article

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

# Create your views here.

def article_create_view(request):
    
    form_a = ArticleModelForm(request.POST or None)
    if form_a.is_valid():
        form_a.save()
        form_a = ArticleModelForm(request.POST or None)
    context = {
        'form': form_a,
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

class ArticleClassCreateView(CreateView):
    template_name = 'articles/articles_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleClassUpdateView(UpdateView):
    template_name = 'articles/articles_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self, queryset=None):
        # this gets the arguemnts inside the url so <int:id>/product/<int:num>/ kwargs would have 
        # 2 arguments id and num/ we can get it like a map
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)

