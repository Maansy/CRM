from rest_framework import viewsets
from .models import Team
from .serializers import TeamSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        return self.queryset.filter(members__in = [self.request.user]).first()

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user)
        obj.save()

@api_view(['GET'])
def get_my_team(request):
    team = Team.objects.filter(members__in = [request.user])
    serializer = TeamSerializer(team, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_member(request):
    team = Team.objects.filter(members__in = [request.user]).first()
    email = request.data['email']
    user = User.objects.filter(username=email).first()
    team.members.add(user)
    team.save()

    return Response({'message': 'Member added successfully'})

