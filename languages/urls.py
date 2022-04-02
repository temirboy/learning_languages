from django.urls import path, include

from . import views

urlpatterns = [
    path('add_language/', views.AddLanguage.as_view(), name='add_language'),
    path('update_language/', views.UpdateLanguage.as_view(), name='update_language'),
    path('delete_language/<int:pk>/remove/', views.DeleteLanguage.as_view(), name='delete_language'),
    #path('delete_language/', views.LanguagesDeleteListView.as_view(), name='delete_language_list'),
    # path('<int:language_id>/', views.VideoYoutubeView.as_view(), name="add_video_youtube1"),
    path('<int:pk>/', views.get_language, name='lang'),
    path('new_words/', views.get_language, name='new_words'),
    path('learned_word/', views.get_language, name='learned_word'),
    # path('list/<int:pk>/', views.get_2),
    path('language_default/', views.my_view, name='language_default'),
    path('select_language/', views.LanguagesListView.as_view(), name='select_language'),
    #path('select_language/', views.select_language, name='select_language'),

]
