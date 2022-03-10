from django.urls import path
from applications.movies.views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view()),
    path('<int:pk>/', MovieDetailView.as_view()),
]
