# Generated by Django 3.1.14 on 2023-07-28 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('is_video_call', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FaceRecognition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_image', models.ImageField(upload_to='face/')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('delivered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('last_online', models.DateTimeField(blank=True, null=True)),
                ('face_recognition', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.facerecognition')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VoiceRecognition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice_file', models.FileField(upload_to='voice/')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voice_recognition',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.voicerecognition'),
        ),
        migrations.CreateModel(
            name='StreamingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('messages', models.ManyToManyField(to='backend.Message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='StatusMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='status_media/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='backend.status')),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile'),
        ),
        migrations.CreateModel(
            name='ScreenSharingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('call', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='screen_sharing_session', to='backend.call')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='backend.userprofile'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='backend.userprofile'),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.group')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='group_memberships', to='backend.UserProfile'),
        ),
        migrations.AddField(
            model_name='facerecognition',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile'),
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_connected', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connections_as_user1', to='backend.userprofile')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connections_as_user2', to='backend.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='call',
            name='caller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_calls', to='backend.userprofile'),
        ),
        migrations.AddField(
            model_name='call',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_calls', to='backend.userprofile'),
        ),
    ]
