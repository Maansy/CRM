from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
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
            'updated_at'
        )