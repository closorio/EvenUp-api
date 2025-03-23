from rest_framework import serializers
from ..models.payment import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'activity', 'payer', 'receiver', 'amount', 'created_at']