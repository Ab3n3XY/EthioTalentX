# Generated by Django 5.0.4 on 2024-05-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatroom_last_message_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
