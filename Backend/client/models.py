from django.db import models
from django.contrib.auth.models import User
from team.models import Team
# Create your models here.

class Client(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='clients', default=1)
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')


    def __str__(self):
        return self.name
