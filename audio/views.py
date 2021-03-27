from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from audio.models import *
import json
from django.http import Http404
from audio import serializers
from django.forms.models import model_to_dict
# Create your views here.

######################################################################################################################################################################
######################################################################################################################################################################



class SongListView(APIView):

    serializer_class = serializers.SongSerializerCreate

    def get(self, request, format=None):

        try:
            """Returns a list of API View features"""
            songs_list = list(Song.objects.all().values())
            return Response({"ok": True, "songs" : songs_list},status=status.HTTP_200_OK)

        except:

            return Response({"ok":False,"songs":None},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SongDetailView(APIView):

    serializer_class = serializers.SongSerializerUpdate

    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        try:
            """Returns a Details of API View features"""
            song_details = self.get_object(pk)
            song_details = model_to_dict(song_details)

            return Response({"ok": True, "song_details" : song_details},status=status.HTTP_200_OK)

        except:
            return Response({"ok":False,"song_details":None},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk, format=None):
        song_details = self.get_object(pk)
        serializer = self.serializer_class(song_details,data=request.data)
        if serializer.is_valid():
            serializer.save()
            song_details = self.get_object(pk)
            song_details = model_to_dict(song_details)
            return Response({"ok": True, "song_details" : song_details},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        song_details = self.get_object(pk)
        song_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



######################################################################################################################################################################
######################################################################################################################################################################



class PodcastListView(APIView):

    serializer_class = serializers.PodcastSerializerCreate

    def get(self, request, format=None):

        try:
            """Returns a list of API View features"""
            podcast_list = list(Podcast.objects.all().values())
            return Response({"ok": True, "podcasts" : podcast_list},status=status.HTTP_200_OK)

        except:

            return Response({"ok":False,"podcasts":None},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PodcastDetailView(APIView):

    serializer_class = serializers.PodcastSerializerUpdate

    def get_object(self, pk):
        try:
            return Podcast.objects.get(pk=pk)
        except Podcast.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        try:
            """Returns a Details of API View features"""
            podcast_details = self.get_object(pk)
            podcast_details = model_to_dict(podcast_details)
            return Response({"ok": True, "podcast_details" : podcast_details},status=status.HTTP_200_OK)

        except:
            return Response({"ok":False,"podcast_details":None},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk, format=None):
        podcast_details = self.get_object(pk)
        serializer = self.serializer_class(podcast_details,data=request.data)
        if serializer.is_valid():
            serializer.save()
            podcast_details = self.get_object(pk)
            podcast_details = model_to_dict(podcast_details)
            return Response({"ok": True, "podcast_details" : podcast_details},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        podcast_details = self.get_object(pk)
        podcast_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


######################################################################################################################################################################
######################################################################################################################################################################



class AudiobookListView(APIView):

    serializer_class = serializers.AudiobookSerializerCreate

    def get(self, request, format=None):

        try:
            """Returns a list of API View features"""
            audiobook_list = list(Audiobook.objects.all().values())
            return Response({"ok": True, "audiobooks" : audiobook_list},status=status.HTTP_200_OK)

        except:

            return Response({"ok":False,"audiobooks":None},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AudiobookDetailView(APIView):

    serializer_class = serializers.AudiobookSerializerUpdate

    def get_object(self, pk):
        try:
            return Audiobook.objects.get(pk=pk)
        except Audiobook.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        try:
            """Returns a Details of API View features"""
            audiobook_details = self.get_object(pk)
            audiobook_details = model_to_dict(audiobook_details)
            return Response({"ok": True, "audiobook_details" : audiobook_details},status=status.HTTP_200_OK)

        except:
            return Response({"ok":False,"audiobook_details":None},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk, format=None):
        audiobook_details = self.get_object(pk)
        serializer = self.serializer_class(audiobook_details,data=request.data)
        if serializer.is_valid():
            serializer.save()
            audiobook_details = self.get_object(pk)
            audiobook_details = model_to_dict(audiobook_details)
            return Response({"ok": True, "audiobook_details" : audiobook_details},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        audiobook_details = self.get_object(pk)
        audiobook_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
