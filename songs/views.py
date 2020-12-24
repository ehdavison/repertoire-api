from django.shortcuts import render
from rest_framework import generics, status
from .models import Song
from .serializers import SongSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.


class SongsList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def post(self, request):
        print(request.data)
        """Create request"""
        # Add user to request data object
        request.data['song']['owner'] = request.user.id
        # Serialize/create song
        song = SongSerializer(data=request.data['song'])
        # If the song data is valid according to our serializer...
        if song.is_valid():
            # Save the created song & send a response
            song.save()
            return Response({'song': song.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(song.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def patch(self, request, pk):
        # print(request.data)
        # """Create request"""
        # # Add user to request data object
        # request.data['song']['owner'] = request.user.id
        # # Serialize/create song
        # song = SongSerializer(data=request.data['song'])
        # # If the song data is valid according to our serializer...
        # if song.is_valid():
        #     # Save the created song & send a response
        #     song.save()
        #     return Response({'song': song.data}, status=status.HTTP_201_CREATED)
        # # If the data is not valid, return a response with the errors
        # return Response(song.errors, status=status.HTTP_400_BAD_REQUEST)

        # instance = self.get_object()
        # instance.song = request.data.get(pk)
        # instance.user = request.data.get(pk)
        # instance
        # serializer = SongSerializer(song, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        # return Response(status=status.HTTP_400_BAD_REQUEST, data='wrong params')
        """Update Request"""
        song = get_object_or_404(Song, pk=pk)
        ms = SongSerializer(song, data=request.data['song'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
