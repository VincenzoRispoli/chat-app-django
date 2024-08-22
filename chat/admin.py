from django.contrib import admin
from .models import Message, Chat

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    """ Customizes the Django admin interface for the Message model.

    This admin class configures how messages are displayed and managed within the Django admin interface.

    Attributes:
        fields (tuple): Specifies the fields to include in the form when adding or editing a Message. 
                        The fields are shown in the order defined in this tuple.
        
        list_display (tuple): Defines the fields to display in the list view of messages within the admin interface. 
                              These fields are shown as columns in the message list view.
        
        search_fields (tuple): Specifies the fields that can be searched through the search box in the 
                               message list view. Only the fields included in this tuple are searchable
    """
    fields = ('text', 'created_at', 'author', 'receiver', 'chat')
    list_display = ('text', 'created_at', 'author', 'receiver', 'chat')
    search_fields = ('text',)
    
class ChatAdmin(admin.ModelAdmin):
    """ Customize the Django model interface fot the Chat model.
    This admin class configures how the Chats models are displayed and managed within the Django admin interface

    Attributes:
        fields (tuple): Specifies the fields to include in the form when adding or editing a Message. 
                        The fields are shown in the order defined in this tuple 
    """
    fields = ('created_at',)
    
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)

