from rest_framework import serializers
from .models import Lead
from team.serializers import UserSerializer

class LeadSerializer(serializers.ModelSerializer):

    assigned_to = UserSerializer(read_only=True)
    class Meta:
        model = Lead
        read_only_fields = ('created_at', 'updated_at', 'created_by')
        fields = (
            'id',
            'company_name',
            'contact_name',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'created_at',
            'updated_at',
            'assigned_to',
        )