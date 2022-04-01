from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from video_youtube.models import VideoUrl
from .forms import AddVideoYoutube

from django.shortcuts import get_object_or_404, get_list_or_404


class AddVideoYoutube(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = VideoUrl
    fields = ['url', 'name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(AddVideoYoutube, self).form_valid(form)

    def form_valid(self, form):
        form.instance.language_id = self.request.language.id
        return super(AddVideoYoutube, self).form_valid(form)


class VideoYoutubeView(ListView):
    model = VideoUrl


def get_1(request, pk: int):
    vid = get_object_or_404(VideoUrl, id=pk)
    return render(request, 'video_youtube/videourl_form.html', {'video': vid})


def get_2(request, pk: int):
    vid1 = get_list_or_404(VideoUrl, user_id=pk)
    return render(request, 'video_youtube/list_video.html', {'video': vid1})


def get_3(request):
    print("get_3")
    print(request.user.id)
    language = request.session.get('language', None)
    if language == None:
        return redirect('../../languages/select_language/')
    vid1 = get_list_or_404(VideoUrl, user_id=request.user.id)
    print(vid1)
    return render(request, 'video_youtube/list_video.html', {'video': vid1})


def add_video_youtube(request):
    if request.method == 'post':
        form = AddVideoYoutube(request.POST)
    else:
        form = AddVideoYoutube()
    return render(request, 'video_youtube/videourl_form.html', {'form': form})

# def add_video_youtube_view(request):
#    return render(request, 'videourl_form.html')
