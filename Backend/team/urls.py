from django.urls import path, include
from rest_framework import routers
from .views import TeamViewSet, get_my_team, add_member, UserDetail, upgrade_plan, get_stripe_pub_key,create_chechout_session, stripe_webhook, check_session

router = routers.DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/member/<int:pk>/', UserDetail.as_view(), name='user-detail'),  
    path('teams/my-team/', get_my_team, name='my-team'),
    path('teams/add-member/', add_member, name='add-member'),
    path('teams/upgrade-plan/', upgrade_plan, name='upgrade-plan'),
    path('stripe/get-stripe-pub-key/', get_stripe_pub_key, name='stripe-pub-key'),
    path('stripe/create-checkout-session/', create_chechout_session, name='create-checkout-session'),
    path('stripe/webhook/', stripe_webhook, name='stripe-webhook'),
    path('stripe/check-session/', check_session, name='check-session'),
    path('', include(router.urls)),
]