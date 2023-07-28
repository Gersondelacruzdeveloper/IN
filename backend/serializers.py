from rest_framework import serializers

from .models import (
    UserProfile, Message, GroupMessage,
    Group, Call, VoiceRecognition,
    FaceRecognition,Connection,
    Status, StatusMedia, ScreenSharingSession,StreamingSession)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'


class VoiceRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceRecognition
        fields = '__all__'

class FaceRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceRecognition
        fields = '__all__'       


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'       

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'   


class StatusMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusMedia
        fields = '__all__'   

class ScreenSharingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenSharingSession
        fields = '__all__'   


class StreamingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenSharingSession
        fields = '__all__'   

