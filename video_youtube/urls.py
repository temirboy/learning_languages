from django.urls import path, include

from . import views

urlpatterns = [
    path('add_video_youtube/', views.AddVideoYoutube.as_view(), name='add_video_youtube'),
    path('<int:user_id>/<int:language_id>/', views.VideoYoutubeView.as_view(), name='add_video_youtube1'),
    #path('<int:pk>/', views.get_1),
    #path('list/<int:pk>/', views.get_2),
    path('list_video/', views.get_3, name='list_video'),
    path('<int:pk>/list_video/', views.VideoYoutubeListView.as_view(), name='lang_list_video'),
]
