from django.urls import path
from applications.movies.views import MovieListView, MovieDetailView, MovieViewSet

urlpatterns = [
    path('', MovieListView.as_view()),
    path('<int:pk>/', MovieDetailView.as_view()),
    path('', MovieViewSet.as_view),
]
