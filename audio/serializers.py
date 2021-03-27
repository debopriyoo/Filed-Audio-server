from rest_framework import serializers
from audio.models import *
from django.utils import timezone
import datetime
from django.core.exceptions import ValidationError

class SongSerializerCreate(serializers.Serializer):


    # id = serializers.IntegerField()
    song_name = serializers.CharField(max_length=100)
    duration = serializers.CharField(max_length=100)
    # upload_time = serializers.DateTimeField(default=timezone.now())

    def create(self, validated_data):
        """Create and return a new `Song` instance, given the validated data."""
        return Song.objects.create(**validated_data)



class SongSerializerUpdate(serializers.Serializer):


    # id = serializers.IntegerField()
    song_name = serializers.CharField(max_length=100,required=False)
    duration = serializers.CharField(max_length=100,required=False)
    # upload_time = serializers.DateTimeField(default=timezone.now())

    def update(self, instance, validated_data):
        """Update and return an existing `Song` instance, given the validated data."""
        # instance.id = validated_data.get('id', instance.id)
        # instance.id = validated_data.get('id', instance.id)
        instance.song_name = validated_data.get('song_name', instance.song_name)
        instance.duration = validated_data.get('duration', instance.duration)
        # instance.upload_time = validated_data.get('upload_time', instance.upload_time)
        # instance.upload_time = datetime.datetime.now()
        instance.save()
        return instance

###################################################################################################################################
###################################################################################################################################


class PodcastSerializerCreate(serializers.Serializer):

    def validate_participant(value):
        value = value.split(',')
        if len(value) > 10:
            raise ValidationError('Maximum 10 participants allowed.')
        else:
            for item in value:
                if len(item)>100:
                    raise ValidationError('participants name are grater than 100 charecter.')
            return value

    # id = serializers.IntegerField()
    podcast_name = serializers.CharField(max_length=100)
    duration = serializers.CharField(max_length=100)
    host = serializers.CharField(max_length=100)
    participants = serializers.CharField(max_length=1100,validators=[validate_participant])
    # upload_time = serializers.DateTimeField(default=timezone.now())


    def create(self, validated_data):
        """Create and return a new `Podcast` instance, given the validated data."""
        return Podcast.objects.create(**validated_data)


class PodcastSerializerUpdate(serializers.Serializer):

    # id = serializers.IntegerField()
    podcast_name = serializers.CharField(max_length=100,required=False)
    duration = serializers.CharField(max_length=100,required=False)
    host = serializers.CharField(max_length=100,required=False)
    participants = serializers.CharField(max_length=1100,required=False,validators=[PodcastSerializerCreate.validate_participant])
    # upload_time = serializers.DateTimeField(default=timezone.now())


    def update(self, instance, validated_data):
        """Update and return an existing `Podcast` instance, given the validated data."""
        # instance.id = validated_data.get('id', instance.id)
        # instance.id = validated_data.get('id', instance.id)
        instance.podcast_name = validated_data.get('podcast_name', instance.podcast_name)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.host = validated_data.get('host', instance.host)
        instance.participants = validated_data.get('participants', instance.participants)
        # instance.upload_time = datetime.datetime.now()
        instance.save()
        return instance


###################################################################################################################################
###################################################################################################################################



class AudiobookSerializerCreate(serializers.Serializer):

    # id = serializers.IntegerField()
    audiobook_name = serializers.CharField(max_length=100)
    duration = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    narrator = serializers.CharField(max_length=100)
    # upload_time = serializers.DateTimeField(default=timezone.now())

    def create(self, validated_data):
        """Create and return a new `audiobook` instance, given the validated data."""
        return Audiobook.objects.create(**validated_data)


class AudiobookSerializerUpdate(serializers.Serializer):

    # id = serializers.IntegerField()
    audiobook_name = serializers.CharField(max_length=100,required=False)
    duration = serializers.CharField(max_length=100,required=False)
    author = serializers.CharField(max_length=100,required=False)
    narrator = serializers.CharField(max_length=100,required=False)
    # upload_time = serializers.DateTimeField(default=timezone.now())


    def update(self, instance, validated_data):
        """Update and return an existing `audiobook` instance, given the validated data."""
        # instance.id = validated_data.get('id', instance.id)
        # instance.id = validated_data.get('id', instance.id)
        instance.audiobook_name = validated_data.get('audiobook_name', instance.audiobook_name)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.author = validated_data.get('author', instance.author)
        instance.narrator = validated_data.get('narrator', instance.narrator)
        # instance.upload_time = datetime.datetime.now()
        instance.save()
        return instance
