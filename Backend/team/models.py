from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    name = models.CharField(max_length=100)
    max_leads = models.IntegerField(default=5)
    max_clients = models.IntegerField(default=5)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Team(models.Model):

    PLAN_ACTIVE = 'active'
    PLAN_CANCELLED = 'cancelled'

    CHOISES_PLAN_STATUS = (
        (PLAN_ACTIVE, 'Active'),
        (PLAN_CANCELLED, 'Cancelled'),
    )

    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='members')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    created_at = models.DateTimeField(auto_now_add=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL,blank=True, null=True, related_name='team')
    plan_status = models.CharField(max_length=20, choices=CHOISES_PLAN_STATUS, default=PLAN_ACTIVE)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)



    def __str__(self):
        return self.name
    
