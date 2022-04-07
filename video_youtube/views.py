from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from video_youtube.models import VideoUrl
from languages.models import Languages
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from django.conf.global_settings import LANGUAGES
from django.db.models.query_utils import DeferredAttribute


class AddVideoYoutube(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = VideoUrl
    fields = ['url', 'name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_id = self.request.user.id
        language = self.request.session.get('language', None)
        if language == None:
            return redirect('../../languages/list_languages/')
        instance.language_id = language
        instance.save()
        return super(AddVideoYoutube, self).form_valid(form)


def video_youtube_list(request):
    language = request.session.get('language', None)
    if language == None:
        return redirect('../../languages/list_languages/')
    video_list = list(VideoUrl.objects.filter(user_id=request.user.id, language_id=language))
    if not video_list:
        return redirect('../add_video_youtube/')
    # video_list = get_list_or_404(VideoUrl, user_id=request.user.id, language_id=language)
    return render(request, 'video_youtube/list_videos.html', {'video_list': video_list})


class DeleteVideoYoutube(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = VideoUrl
    success_url = reverse_lazy('list_videos')


class VideoSubtitlesYoutube():
    srt = 'qw'

    def get_list_subtitles_en(self, url, lang):
        self.url = url
        yt = YouTube(url)
        transcript_list = YouTubeTranscriptApi.list_transcripts(yt.video_id)
        transcript_list_code = [t.language_code for t in transcript_list]
        if lang not in transcript_list_code:
            print('такого языка нет')
            return None
        transcript = transcript_list.find_transcript([lang])
        return transcript.fetch()

    def get_list_subtitles_ru(self, url, lang):
        self.url = url
        yt = YouTube(url)
        transcript_list = YouTubeTranscriptApi.list_transcripts(yt.video_id)
        transcript_list_code = [t.language_code for t in transcript_list]
        if lang not in transcript_list_code:
            print('такого языка нет')
            return None
        transcript = transcript_list.find_transcript([lang])
        translated_transcript = transcript.translate('ru')
        return translated_transcript.fetch()


class VideoSubtitlesDetailView(DetailView):
    model = VideoUrl
    template_name = 'video_youtube/video_subtitles.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lang_ = Languages.objects.filter(id=self.request.session.get('language'))
        url_id = self.kwargs.get(self.pk_url_kwarg, None)
        url_ = VideoUrl.objects.filter(id=url_id)
        context['latest_en'] = VideoSubtitlesYoutube().get_list_subtitles_en(url_[0].url,lang_[0].name)
        context['latest_ru'] = VideoSubtitlesYoutube().get_list_subtitles_ru(url_[0].url,lang_[0].name)
        return context


def play_video(request):
    return render(request, 'video_youtube/play_video.html', {'video_list': "test_test"})


# class VideoYoutubeListView(LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     model = VideoUrl
#     template_name = 'video_youtube/list_videos.html'
#
#     # quryset = Languages.objects.filter(user_id=self.request.user.id)
#
#     # request.session['username1'] = 'qwe'
#     # request.session.modified = True
#     def get_queryset(self):
#         print("VideoYoutubeListView")
#         print('user - ', self.request.user.id)
#         language = self.request.session.get('language', None)
#         print('lang - ', language)
#         if language == None:
#             print('none ', language)
#             return redirect('../../languages/list_languages/')
#         video_list = VideoUrl.objects.filter(
#             user_id=self.request.user.id,
#             language_id=language
#         )
#         return video_list
