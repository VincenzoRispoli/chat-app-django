from django.contrib import admin
from .models import Message, Chat

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    fields = ('text', 'created_at', 'author', 'receiver', 'chat')
    list_display = ('text', 'created_at', 'author', 'receiver', 'chat')
    search_fields = ('text',)
    
class ChatAdmin(admin.ModelAdmin):
    fields = ('created_at',)
    
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)

