from django.urls import path, include

from . import views

urlpatterns = [
    path('add_language/', views.add_language, name='add_language'),
    # path('<int:language_id>/', views.VideoYoutubeView.as_view(), name="add_video_youtube1"),
    path('<int:pk>/', views.get_language),
    # path('list/<int:pk>/', views.get_2),
]
