from django.shortcuts import render, redirect
from django.views.generic import ListView
from video_youtube.models import VideoUrl
from .forms import AddVideoYoutube

from django.shortcuts import get_object_or_404, get_list_or_404


class VideoYoutubeView(ListView):
    model = VideoUrl


def get_1(reguest, pk: int):
    vid = get_object_or_404(VideoUrl, id=pk)
    return render(reguest, 'video_youtube/add_video_youtube.html', {'video': vid})


def get_2(reguest, pk: int):
    vid1 = get_list_or_404(VideoUrl, user_id=pk)
    return render(reguest, 'video_youtube/list_video.html', {'video': vid1})


def add_video_youtube(request):
    if request.method == 'post':
        form = AddVideoYoutube(request.POST)
    else:
        form = AddVideoYoutube()
    return render(request, 'video_youtube/add_video_youtube.html', {'form': form})

# def add_video_youtube_view(request):
#    return render(request, 'add_video_youtube.html')
