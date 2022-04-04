from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from video_youtube.models import VideoUrl
from .forms import AddVideoYoutube



class AddVideoYoutube(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = VideoUrl
    fields = ['url', 'name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.language_id = self.request.session.get('language', None)
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
