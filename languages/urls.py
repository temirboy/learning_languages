from django.urls import path, include

from . import views

urlpatterns = [
    path('add_language/', views.AddLanguage.as_view(), name='add_language'),
    path('update_language/', views.UpdateLanguage.as_view(), name='update_language'),
    path('<int:user_id>/delete_language/', views.DeleteLanguage.as_view(), name='delete_language'),
    # path('<int:language_id>/', views.VideoYoutubeView.as_view(), name="add_video_youtube1"),
    path('<int:pk>/', views.get_language),
    # path('list/<int:pk>/', views.get_2),
    path('language_default/', views.my_view, name='language_default'),
    path('select_language/', views.select_language, name='select_language'),

]
