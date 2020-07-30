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
from tunefinder.TuneFinder_PythonCode import TuneFinder
# Create your views here.


def homepage(request):
    return render(request, 'tunefinder/homepage.html', {'songs': ['All Star', 'Wonder Wall', 'Beat it']})


def search(request):
    return render(request, 'tunefinder/Search.html', {})


def song(request, added_context=None):
    context = {}
    song_list = "song_list"
    if added_context:
        if added_context[song_list] and len(added_context[song_list]) > 0:
            this_context = added_context[song_list]
            print(this_context)
            this_context = [songInfo(x, y) for (x, y) in this_context]
            context[song_list] = this_context

    return render(request, 'tunefinder/song.html', context)


class songInfo:
    def __init__(self, percent: float, name: str):
        self.percent = round(percent*100, 3)
        self.name = name


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = str(
                (datetime.now() - datetime(1970, 1, 1)).total_seconds())+".wav"
            file_path = os.path.join('media', file_name)
            if not os.path.exists('media'):
                os.mkdir("media")
            handle_uploaded_file(request.FILES['file'], file_path)
            # return HttpResponseRedirect(reverse('homepage'))
            results = TuneFinder.main("model.m", file_path)
            # results = [(0.5, "All Star"), (0.5, "Half Star")]
            print(results)
            return song(request, added_context={"song_list": results})
        else:
            pass
    else:
        form = UploadFileForm()
    return render(request, 'tunefinder/upload.html', {'form': form})
