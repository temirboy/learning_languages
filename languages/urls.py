from django.urls import path, include

from . import views

urlpatterns = [
    path('add_language/', views.AddLanguage.as_view(), name='add_language'),
    path('delete_language/<int:pk>/remove/', views.DeleteLanguage.as_view(), name='delete_language'),
    path('<int:pk>/', views.get_language, name='lang'),
    path('list_languages/', views.LanguagesListView.as_view(), name='list_languages'),

]
