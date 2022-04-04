from django.urls import path

from . import views

urlpatterns = [
    path('add_video_youtube/', views.AddVideoYoutube.as_view(), name='add_video_youtube'),
    path('delete_language/<int:pk>/remove/', views.DeleteVideoYoutube.as_view(), name='delete_video_youtube'),
    path('list_videos/', views.video_youtube_list, name='list_videos'),
]
