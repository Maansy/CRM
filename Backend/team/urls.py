from django.urls import path, include
from rest_framework import routers
from .views import TeamViewSet, get_my_team, add_member

router = routers.DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/my-team/', get_my_team, name='my-team'),
    path('teams/add-member/', add_member, name='add-member'),

    path('', include(router.urls)),
]