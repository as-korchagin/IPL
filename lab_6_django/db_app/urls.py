from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:id>', views.book_detail, name='book'),
    path('author/<int:id>', views.author_detail, name='author'),
    path('genre/<int:id>', views.genre_detail, name='genre'),
]
