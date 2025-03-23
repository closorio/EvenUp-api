from django.db import models
from .event import Event
from .user import User

class Invitation(models.Model):
    INVITATION_STATES = [
        ('PENDING', 'Pendiente'),
        ('ACCEPTED', 'Aceptada'),
        ('REJECTED', 'Rechazada'),
    ]

    event = models.ForeignKey(Event, related_name='invitations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='invitations', on_delete=models.CASCADE)
    invitation_state = models.CharField(max_length=10, choices=INVITATION_STATES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')

    def __str__(self):
        return f"{self.user.email} -> {self.event.name}"