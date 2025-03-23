from rest_framework import serializers
from ..models.contact import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'user', 'contact', 'created_at']