from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Lead
from .serializers import LeadSerializer



class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.leads.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)