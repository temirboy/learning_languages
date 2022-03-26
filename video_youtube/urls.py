from django.urls import path, include

from . import views

urlpatterns = [
    path('add_video/', views.add_video_youtube, name='add_video_youtube'),
    path('<int:user_id>/<int:language_id>/', views.VideoYoutubeView.as_view(), name='add_video_youtube1'),
    path('<int:pk>/', views.get_1),
    path('list/<int:pk>/', views.get_2),
]
