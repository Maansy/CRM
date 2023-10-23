from django.db import models
from django.contrib.auth.models import User
from team.models import Team
# Create your models here.

class Lead(models.Model):
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'In Progress'),
        (LOST, 'Lost'),
        (WON, 'Won'),
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leads', default=1)
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(max_length=100, blank=True, null=True, choices=CHOICES_PRIORITY, default=MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='leads_assigned', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leads')


    def __str__(self):
        return self.company_name
