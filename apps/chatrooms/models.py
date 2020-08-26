from django.db import models
import uuid
from uuid import UUID


class Room(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    room_name: str = models.TextField(default="")
    password: str = models.TextField(default="")
    
