from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView
from video_youtube.models import VideoUrl


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


class VideoSubtitles(View):
    def get(self, request, pk):
        video_subtitles = VideoUrl.objects.get(id=pk)
        return render(request,'video_youtube/video_subtitles.html', {'video_subtitles':video_subtitles})

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
