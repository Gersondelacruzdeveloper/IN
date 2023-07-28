from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import get_resolver
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.http import Http404
# from .utils import compare_data


from .models import (
    UserProfile, Message, GroupMessage,
    Group, Call, VoiceRecognition,
    FaceRecognition, Connection,
    Status, StatusMedia, ScreenSharingSession, StreamingSession)

from .serializers import (UserProfileSerializer, MessageSerializer,
                          GroupMessageSerializer, GroupSerializer,
                          CallSerializer, VoiceRecognitionSerializer,
                          FaceRecognitionSerializer, ConnectionSerializer,
                          StatusSerializer, StatusMediaSerializer,
                          ScreenSharingSessionSerializer, StreamingSessionSerializer,
                          )


# @api_view(['POST'])
# @login_required
# def authenticate_user(request):
#     # Process voice and face data
#     voice_data = request.data.get('voice_data')
#     face_data = request.data.get('face_data')

#     # Retrieve stored authentication data for the logged-in user
#     user_profile = request.user.profile
#     print('user_profile', user_profile)
#     # stored_voice_data = user_profile.voice_recognition
#     # stored_face_data = user_profile.face_recognition

#     # Implement authentication logic by comparing voice_data and face_data with the stored authentication data
#     if stored_voice_data and stored_face_data:
#         if compare_data(voice_data, stored_voice_data, face_data, stored_face_data):
#             return Response({'success': 'User authenticated successfully.'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Authentication failed.'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
def get_users(request):
    users = UserProfile.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_message(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_group_message(request):
    group_message = GroupMessage.objects.all()
    serializer = GroupMessageSerializer(group_message, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_group(request):
    group = Group.objects.all()
    serializer = GroupSerializer(group, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_call(request):
    call = Call.objects.all()
    serializer = CallSerializer(call, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def get_voice_recognition(request):
    voice_recognition = VoiceRecognition.objects.all()
    serializer = VoiceRecognitionSerializer(voice_recognition, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_face_recognition(request):
    face_recognition = FaceRecognition.objects.all()
    serializer = FaceRecognitionSerializer(face_recognition, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_Connection(request):
    connection = Connection.objects.all()
    serializer = ConnectionSerializer(connection, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_status(request):
    status = Status.objects.all()
    serializer = StatusSerializer(status, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_status_media(request):
    status_media = StatusMedia.objects.all()
    serializer = StatusMediaSerializer(status_media, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_screen_sharing_session(request):
    screen_sharing_session = ScreenSharingSession.objects.all()
    serializer = ScreenSharingSessionSerializer(
        screen_sharing_session, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_streaming_session(request):
    screen_sharing_session = StreamingSession.objects.all()
    serializer = StreamingSessionSerializer(screen_sharing_session, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_users(request):
    users = UserProfile.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_connected_users(request):
    try:
        current_user = request.user
        user_profile = get_object_or_404(UserProfile, user=current_user)
        
        connected_users = UserProfile.objects.filter(
            Q(connections_as_user1__user2=user_profile, connections_as_user1__is_connected=True) |
            Q(connections_as_user2__user1=user_profile, connections_as_user2__is_connected=True)
        ).distinct()

        serializer = UserProfileSerializer(connected_users, many=True)  # Serialize the connected users
        serialized_data = serializer.data  # Get the serialized data
        return Response(serialized_data)
    
    except Http404:
        return Response({'error': 'you have no connected users'}, status=404)

    except Exception as e:
        return Response({'error': 'An error occurred'}, status=500)


