from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Song
from .serializers import SongSerializer
# Create your views here.


class SongsList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
