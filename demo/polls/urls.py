from django.urls import re_path,path


from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('temo', views.index),
    path('createBook/', views.add_books, name = 'addBook'),
    path('createAuthor/', views.add_authors, name = "addAuthor")
]