from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone
import base64
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # other fields
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='profile_images/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    face_recognition = models.OneToOneField(
        'FaceRecognition', on_delete=models.CASCADE, null=True, blank=True)
    voice_recognition = models.OneToOneField(
        'VoiceRecognition', on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    last_online = models.DateTimeField(blank=True, null=True)


    def mark_online(self):
        # Update the last_online field to the current time
        self.last_online = timezone.now()
        self.save()

    
    def __str__(self):
        return str(self.user)  # Return the string representation of the associated User instance


class Message(models.Model):
    sender = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return str(self.sender)  # Convert to string to avoid TypeError


class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(UserProfile, related_name='group_memberships')

    def __str__(self):
        return str(self.name)


class GroupMessage(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.group)


class Media(models.Model):
    file = models.FileField(upload_to='media/')
    uploaded_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file)


class Call(models.Model):
    caller = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='outgoing_calls')
    receiver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='incoming_calls')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    is_video_call = models.BooleanField(default=False)

    def __str__(self):
        return str(self.caller)  # Convert to string to avoid TypeError


class VoiceRecognition(models.Model):
    voice_file = models.FileField(upload_to='voice/')
    speaker = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.speaker)


class FaceRecognition(models.Model):
    face_image = models.ImageField(upload_to='face/')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Status(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    def is_expired(self):
        from datetime import datetime, timedelta
        expiration_time = self.timestamp + timedelta(hours=24)
        return datetime.now() > expiration_time

\
# The StatusMedia model represents the media associated
#  with a status. It contains a foreign key to the Status
#  model, a file field to store the uploaded media, 
# and a timestamp to track when the media was added. 
# The __str__ method returns a string representation 
# of the associated status object.

class StatusMedia(models.Model):
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name='media')
    media = models.FileField(upload_to='status_media/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.status)


class ScreenSharingSession(models.Model):
    call = models.OneToOneField(
        Call, on_delete=models.CASCADE, related_name='screen_sharing_session')
    session_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.session_id)


class Connection(models.Model):
    user1 = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='connections_as_user1')
    user2 = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='connections_as_user2')
    is_connected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.user1} <-> {self.user2} ({'Connected' if self.is_connected else 'Not Connected'})")


class StreamingSession(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    messages = models.ManyToManyField(Message)

    def __str__(self):
        return str(self.user)

    def start_streaming(self):
        # Set the start time and activate the streaming session
        self.start_time = timezone.now()
        self.is_active = True
        self.save()

    def end_streaming(self):
        # Set the end time and deactivate the streaming session
        self.end_time = timezone.now()
        self.is_active = False
        self.save()