from rest_framework import viewsets, permissions
from ..serializers.invitation import InvitationSerializer
from ..models.invitation import Invitation

class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [permissions.IsAuthenticated]