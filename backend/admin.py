from django.contrib import admin

# Register your models here.
from .models import (
    UserProfile, Message, GroupMessage,
    Group, Call, VoiceRecognition,
    FaceRecognition,Connection,
    Status, StatusMedia, ScreenSharingSession, StreamingSession)

admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(Group)
admin.site.register(GroupMessage)
admin.site.register(Call)
admin.site.register(VoiceRecognition)
admin.site.register(StatusMedia)
admin.site.register(Status)
admin.site.register(FaceRecognition)
admin.site.register(ScreenSharingSession)
admin.site.register(Connection)
admin.site.register(StreamingSession)
