from rest_framework import viewsets, permissions
from ..serializers.event import EventSerializer
from ..models.event import Event

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]