from rest_framework import serializers
from ..models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'nickname', 'avatar', 'is_active']