from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('upload', views.upload_file, name='upload'),
    path('search', views.search, name='Search'),
]

#query =""
#if request.GET:
#    query= request.GET['search']
#    context['query']= str(query)