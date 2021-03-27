from django.urls import path, include
from rest_framework.routers import DefaultRouter
from audio import views

urlpatterns = [
    path('song/', views.SongListView.as_view()),
    path('song/<int:pk>/', views.SongDetailView.as_view()),
    path('podcast/', views.PodcastListView.as_view()),
    path('podcast/<int:pk>/', views.PodcastDetailView.as_view()),
    path('audiobook/', views.AudiobookListView.as_view()),
    path('audiobook/<int:pk>/', views.AudiobookDetailView.as_view()),
]
