from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Login view
    path('videos/', views.playlist_view, name='playlist'),  # Video playlist view
]