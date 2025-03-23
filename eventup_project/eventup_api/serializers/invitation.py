from rest_framework import serializers
from ..models.invitation import Invitation

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ['id', 'event', 'user', 'invitation_state', 'created_at']