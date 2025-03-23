from rest_framework import viewsets, permissions
from ..serializers.payment import PaymentSerializer
from ..models.payment import Payment

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]