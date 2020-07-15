from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('upload', views.upload_file, name='upload')
]
