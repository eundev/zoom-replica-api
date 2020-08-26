from rest_framework import viewsets
from apps.chatrooms.models import Room
from apps.chatrooms.serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
