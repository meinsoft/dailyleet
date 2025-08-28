from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.VideoListView.as_view(), name='list'),
    path('<slug:slug>/', views.VideoDetailView.as_view(), name='detail'),
    path('tag/<slug:slug>/', views.TaggedVideoListView.as_view(), name='tagged'),
]