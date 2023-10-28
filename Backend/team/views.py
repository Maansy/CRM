from rest_framework import viewsets, status
from .models import Team, Plan
from .serializers import TeamSerializer,UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.conf import settings
import json
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe

from datetime import datetime
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        return self.queryset.filter(members__in = [self.request.user]).first()

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user)
        obj.save()

class UserDetail(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self,request,pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_stripe_pub_key(request):
    pub_key = settings.STRIPE_PUB_KEY
    return Response({'pub_key': pub_key})


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


@api_view(['POST'])
def upgrade_plan(request):
    team = Team.objects.filter(members__in = [request.user]).first()
    plan = request.data['plan']
    print("plan",plan)
    if plan == 'free':
        plan = Plan.objects.get(name='Free')
    elif plan == 'smallTeam':
        plan = Plan.objects.get(name='Small Team')
    elif plan == 'bigTeam':
        plan = Plan.objects.get(name='Big Team')
    
    team.plan = plan
    team.save()

    serializer = TeamSerializer(team)
    return Response(serializer.data)

@api_view(['POST'])
def create_chechout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = json.loads(request.body)
    plan = data['plan']

    if plan == 'smallTeam':
        price_id = settings.STRIPE_PRICE_ID_SMALL_TEAM
    else:
        price_id = settings.STRIPE_PRICE_ID_BIG_TEAM

    team = Team.objects.filter(members__in = [request.user]).first()

    try:
        checkout_session = stripe.checkout.Session.create(
            success_url = '%s?session_id={CHECKOUT_SESSION_ID}' % settings.FRONTEND_WEBSITE_SUCCESS_URL ,
            cancel_url = '%s' % settings.FRONTEND_WEBSITE_CANCEL_URL,
            payment_method_types = ['card'],
            mode = 'subscription',
            line_items = [
                {
                    'price': price_id,
                    'quantity': 1
                }
            ],
        )
        return Response({'sessionId': checkout_session['id']})

    except Exception as e:
        return Response({'error': str(e)})
    
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_key = settings.STRIPE_WEBHOOK_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    # print("payload",payload)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_key
        )
    except ValueError as e:
        print("value error",e)
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError as e:
        print("signature error",e)
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        team = Team.objects.get(pk=1)
        
        team.stripe_customer_id = 10
        team.stripe_subscription_id = session.get('subscription')
        team.save()

    return HttpResponse(status=200)


@api_view(['POST'])
def check_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    error = ''

    try:
        team = Team.objects.filter(members__in = [request.user]).first()
        subscription = stripe.Subscription.retrieve(team.stripe_subscription_id)
        product = stripe.Product.retrieve(subscription.plan.product)
        team.plan_status = Team.PLAN_ACTIVE
        team.plan_end_date = datetime.fromtimestamp(subscription.current_period_end)
        team.plan = Plan.objects.get(name=product.name)
        team.save()
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    except Exception as e:
        error = str(e)
        return Response({'error': error})