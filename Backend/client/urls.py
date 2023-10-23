from django.urls import path, include
from rest_framework import routers
from .views import ClientViewSet

router = routers.DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
]
