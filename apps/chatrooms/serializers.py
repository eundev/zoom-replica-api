from rest_framework import serializers
from apps.chatrooms.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "room_name", "password")