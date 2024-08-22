from datetime import date
from django.db import models
from django.conf import settings

# Create your models here.
# class Chat(models.Model):
#     created_at = models.DateField(default = date.today)

class Chat(models.Model):
    """ This model create an instance of the class Chat, with a 
        created_at field, that contain the date of the chat creation;

    Args:
        models (Chat): The Chat model instance to be saved in the database
    """
    created_at = models.DateField(default = date.today)
    
class Message(models.Model):
    """ This model create an intance of the class Message, with a:
        - text field, that contain the message;
        - created_at field, that contain the date of creation;
        - chat field, that contain the specific chat it refers to;
        - author field, that contain the message author;
        - receiver field, that contain the message receiver;
    Args:
        models (Message): The Message model instance to be saved in the database
    """
    text = models.CharField(max_length = 500)
    created_at = models.DateField( default = date.today)
    chat = models.ForeignKey(Chat, on_delete = models.CASCADE, related_name = 'chat_message_set', default = None, blank = True, null = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'receiver_message_set')
    
