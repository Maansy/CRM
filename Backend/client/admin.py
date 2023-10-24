from django.contrib import admin
from .models import Client, Note

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'email', 'phone', 'website', 'created_at', 'updated_at', 'created_by')
    search_fields = ('name', 'contact_name', 'email', 'phone', 'website', 'created_at', 'updated_at', 'created_by')

admin.site.register(Client, ClientAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'client', 'created_at', 'updated_at')
    search_fields = ('name', 'body', 'client', 'created_at', 'updated_at')

admin.site.register(Note, NoteAdmin)