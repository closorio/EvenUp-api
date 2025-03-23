from django.db import models
from .user import User

class Event(models.Model):
    EVENT_TYPES = [
        ('TRIP', 'Viaje'),
        ('HOME', 'Hogar'),
        ('COUPLE', 'Pareja'),
        ('FOOD', 'Comida'),
        ('OTHER', 'Otro'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    avatar = models.ImageField(upload_to='event_avatars/', null=True, blank=True)
    creator = models.ForeignKey(User, related_name='created_events', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name