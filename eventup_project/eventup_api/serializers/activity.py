from rest_framework import serializers
from ..models.activity import Activity, Participation

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'event', 'description', 'value', 'created_by', 'created_at']

class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ['id', 'activity', 'user', 'percentage', 'fixed_value']