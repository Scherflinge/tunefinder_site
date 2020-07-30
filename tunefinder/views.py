import os
from django.http import HttpResponseRedirect
from .upload_file import handle_uploaded_file
from .forms import UploadFileForm
from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from datetime import datetime
from django.urls import reverse
# Create your views here.


def homepage(request):
    return render(request, 'tunefinder/homepage.html', {'songs': ['All Star', 'Wonder Wall', 'Beat it']})


def search(request):
    return render(request, 'tunefinder/Search.html', {})


def song(request, added_context={}):
    context = {}
    if request.method == 'POST' and 'song_list' in request.POST:
        if len(request.POST['song_list']) > 0:
            context["song_list"] = [songInfo(x, y)
                                    for (x, y) in request.POST['song_list']]

    return render(request, 'tunefinder/song.html', context)


class songInfo:
    def __init__(self, percent: float, name: str):
        self.percent = round(percent*100, 3)
        self.name = name


def upload_file(request):
    print(os.name)
    if request.method == 'POST':
        print("its post")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], str(1))
            # return HttpResponseRedirect(reverse('homepage'))
            return song(request)
        else:
            print("invalid form")
    else:
        form = UploadFileForm()
    return render(request, 'tunefinder/upload.html', {'form': form})
