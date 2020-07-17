from django.http import HttpResponseRedirect
from .upload_file import handle_uploaded_file
from .forms import UploadFileForm
from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return render(request, 'tunefinder/homepage.html', {'songs':['All Star', 'Wonder Wall', 'Beat it']})


def search(request):
    return render(request, 'tunefinder/Search.html', {})

def get_search(query=None)
    queryset= []
    queries = query.split(" ")
    for q in queries:
        Search = Tune.objects.filter(
            Q(title_icontrains=q)
            Q(body_Iconstrains=q)
        ).distinct()


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'tunefinder/upload.html', {'form': form})
