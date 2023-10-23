from django.contrib import admin
from .models import Client
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'email', 'phone', 'website', 'created_at', 'updated_at', 'created_by')
    search_fields = ('name', 'contact_name', 'email', 'phone', 'website', 'created_at', 'updated_at', 'created_by')

admin.site.register(Client, ClientAdmin)