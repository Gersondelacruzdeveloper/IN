from django.urls import path, include
from . import views


urlpatterns = [
    path('users/', views.get_users),
    path('message/', views.get_message),
    path('group-message/', views.get_group_message),
    path('group/', views.get_group),
    path('call/', views.get_call),
    path('voice-recognition/', views.get_voice_recognition),
    path('face-recognition/', views.get_face_recognition),
    path('connection/', views.get_Connection),
    path('status/', views.get_status),
    path('status-media/', views.get_status_media),
    path('screen-sharing-session/', views.get_screen_sharing_session),
    path('streaming_session/', views.get_streaming_session),
    path('get_connected_users/', views.get_connected_users),
]
