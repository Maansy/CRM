from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Lead
from .serializers import LeadSerializer
from team.models import Team
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination 

class LeadPagination(PageNumberPagination):
    page_size = 10

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    pagination_class = LeadPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('company_name','contact_name')

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)
    
    def perform_update(self, serializer):
        obj = self.get_object()
        member_id = self.request.data['assigned_to']
        if member_id:
            user = User.objects.get(id=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team = team,created_by=self.request.user)