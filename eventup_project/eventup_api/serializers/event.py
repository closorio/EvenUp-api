from rest_framework import serializers
from ..models.event import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'event_type', 'avatar', 'creator', 'created_at']