from rest_framework import serializers
from .models import Client, Note

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = ('created_at', 'updated_at', 'created_by')
        fields = (
            'id',
            'name',
            'contact_name',
            'email',
            'phone',
            'website',
            'created_at',
            'updated_at',
        )

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        read_only_fields = ('created_at', 'updated_at')
        fields = (
            'id',
            'name',
            'body',
            'client',
            'created_at',
            'updated_at',
        )