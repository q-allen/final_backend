from django.urls import path
from .views import (
    MovieListCreateView, MovieRetrieveUpdateDestroyView,
    RatingListCreateView, RatingRetrieveUpdateDestroyView,
    ReviewListCreateView, ReviewRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', MovieListCreateView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),

    path('ratings/', RatingListCreateView.as_view(), name='rating-list'),
    path('ratings/<int:pk>/', RatingRetrieveUpdateDestroyView.as_view(), name='rating-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),
]
