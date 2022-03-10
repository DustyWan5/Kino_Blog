from django.urls import path

from applications.genre.views import GenreListView

urlpatterns = [
    path('genre-list/', GenreListView.as_view())
]
