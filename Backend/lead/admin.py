from django.contrib import admin

# Register your models here.

from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'email', 'phone', 'website', 'confidence', 'estimated_value', 'status', 'priority', 'created_at', 'updated_at', 'created_by')
    list_filter = ('status', 'priority', 'created_at', 'updated_at', 'created_by')
    search_fields = ('company_name', 'contact_name', 'email', 'phone', 'website', 'confidence', 'estimated_value', 'status', 'priority', 'created_at', 'updated_at', 'created_by')

admin.site.register(Lead, LeadAdmin)
