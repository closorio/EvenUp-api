from django.db import models
from .event import Event
from .user import User

class Activity(models.Model):
    event = models.ForeignKey(Event, related_name='activities', on_delete=models.CASCADE)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, related_name='created_activities', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Participation(models.Model):
    activity = models.ForeignKey(Activity, related_name='participations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='participations', on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fixed_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('activity', 'user')

    def __str__(self):
        return f"{self.user.email} -> {self.activity.description}"