from django.urls import path
from . import views
from .views import post_list, post_detail, posts_by_author, add_post
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),  # існуючий список постів
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # детальна сторінка посту
    path('author/<int:author_id>/', views.posts_by_author, name='posts_by_author'),  # пости за автором
    path('add_post/', add_post, name='add_post'),
]