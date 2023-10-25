from django.urls import path, include
from rest_framework import routers
from .views import ClientViewSet, NoteViewSet, convert_lead_to_client

router = routers.DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('convert-lead-to-client/', convert_lead_to_client, name='convert-lead-to-client'),
    path('', include(router.urls)),
]
