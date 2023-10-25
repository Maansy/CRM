from rest_framework import viewsets,status, filters
from .models import Client, Note
from .serializers import ClientSerializer, NoteSerializer
from team.models import Team
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from lead.models import Lead
from team.models import Team
from rest_framework.pagination import PageNumberPagination

class ClientPagination(PageNumberPagination):
    page_size = 10

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','contact_name')


    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)
    
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team = team,created_by=self.request.user)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.GET.get('client')
        return self.queryset.filter(team = team).filter(client_id=client_id)
    
        
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client']
        serializer.save(team = team,created_by=self.request.user, client_id=client_id)


@api_view(['POST'])
def convert_lead_to_client(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']
    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        return Response({'message': 'Lead does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    client = Client.objects.create(team=team,name=lead.company_name, 
                                   contact_name=lead.contact_name, phone = lead.phone, 
                                   email=lead.email, website=lead.website, created_by=request.user)
    return Response()