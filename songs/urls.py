from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.SongsList.as_view(), name='songs_list'),
    path('<int:pk>/', views.SongDetail.as_view(), name='song_detail'),
]
