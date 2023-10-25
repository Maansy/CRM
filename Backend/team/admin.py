from django.contrib import admin
from .models import Team, Plan

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    list_filter = ('created_by', 'created_at')
    search_fields = ('name', 'created_by', 'created_at')

admin.site.register(Team, TeamAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_leads', 'max_clients', 'price')
    list_filter = ('name', 'max_leads', 'max_clients', 'price')
    search_fields = ('name', 'max_leads', 'max_clients', 'price')

admin.site.register(Plan, PlanAdmin)