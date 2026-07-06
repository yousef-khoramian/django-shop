from . import views
from django.urls import path

urlpatterns=[
    path('',views.ArticleListView.as_view(),name='article_list_page'),
    path('<slug>/',views.ArticleDetailView.as_view(),name='article_detail_page'),
    path('comments',views.article_comments,name='article_comments'),
]