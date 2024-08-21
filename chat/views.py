from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Message, Chat
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.serializers import serialize

# Create your views here.
@login_required(login_url = '/login/')
def index(request):
    myChat = Chat.objects.get(id = 1)
    if request.method == 'POST':
        message = request.POST['textmessage']
        new_message =  Message.objects.create(text = message, chat = myChat, author = request.user, receiver = request.user )
        serialized_obj = serialize('json', [new_message, ])
        return JsonResponse(serialized_obj[1:-1], safe = False)
    chatMessages = Message.objects.filter(chat__id = 1) # con chat__id andiamo a predere l'oggetto chat dell'oggetto parent Message, in cui id é 1
    return render(request, 'chat/chat.html', {'messages' : chatMessages})


def loginView(request):
    redirect = request.GET.get('next','/chat/')
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
        if user:
            login(request, user)
            return JsonResponse({'status': 'success', 'url': '/chat/'})
        else:
            return JsonResponse({'status': 'error'}, status = 401)
    return render(request, 'auth/login.html', {'redirect': redirect})



def registerView(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST.get("username"), email = request.POST.get("email"), password = request.POST.get("password"))
        user.is_staff = True
        user.save()
        return JsonResponse({'status': 'success', 'url': '/chat/'})
    return render(request, 'auth/register.html')



# def loginView(request):
#     redirect = request.GET.get('next','/chat/')
#     if request.method == 'POST':
#         user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
#         if user:
#             login(request, user)
#             return JsonResponse(request.POST.get('redirect'))
#         else:
#             return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
#     return render(request, 'auth/login.html', {'redirect': redirect})