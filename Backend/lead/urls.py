from django.urls import path, include
from rest_framework import routers
from .views import LeadViewSet

router = routers.DefaultRouter()
router.register('leads', LeadViewSet, basename='leads')

urlpatterns = [
    path('', include(router.urls)),
]
