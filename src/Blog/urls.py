from django.urls import path
from .views import (
    article_create_view,
    article_detail_view,
    article_list_view,
    ArticleClassListView,
    ArticleClassDetailView,
    ArticleClassCreateView,
    ArticleClassUpdateView,
)

urlpatterns = [
    path('create/', article_create_view, name = 'article-create'),
    path('<int:id>/', article_detail_view, name = 'article-detail'),
    path('list/', article_list_view, name = 'article-list'),
    path('listclass/', ArticleClassListView.as_view(), name = 'article-list-class'),
    path('detailclass/<int:id>', ArticleClassDetailView.as_view(), name = 'article-detail-class'),
    path('createclass/', ArticleClassCreateView.as_view(), name = 'article-create-class'),
    path('updateclass/', ArticleClassUpdateView.as_view(), name = 'article-update-class'),
]
