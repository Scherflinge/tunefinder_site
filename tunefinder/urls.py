from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('upload', views.upload_file, name='upload'),
    path('search', views.search, name='Search'),
    path('song', views.song, name='song'),
]

