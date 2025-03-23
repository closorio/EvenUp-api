from rest_framework import viewsets, permissions
from ..serializers.contact import ContactSerializer
from ..models.contact import Contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]