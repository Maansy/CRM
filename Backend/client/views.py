from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from team.models import Team

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)
    
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team = team,created_by=self.request.user)