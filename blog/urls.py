from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='posts-list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('authors/', views.author_list, name='author_list'),
    path('autors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('tags/', views.tags_list, name='tags-list'),
    path('tags/<str:tag_name>/', views.tag_posts, name='tag-posts'),
]
