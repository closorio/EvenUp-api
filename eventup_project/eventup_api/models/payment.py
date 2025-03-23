from django.db import models
from .activity import Activity
from .user import User

class Payment(models.Model):
    activity = models.ForeignKey(Activity, related_name='payments', on_delete=models.CASCADE)
    payer = models.ForeignKey(User, related_name='payments_made', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='payments_received', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payer.email} -> {self.receiver.email}: {self.amount}"