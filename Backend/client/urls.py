from django.urls import path, include
from rest_framework import routers
from .views import ClientViewSet, NoteViewSet

router = routers.DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('', include(router.urls)),
]
