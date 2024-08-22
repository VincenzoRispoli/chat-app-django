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
    """ Handles the display of chat messages and the creation of new messages in the chat.
    This view is responsible for rendering the chat interface and processing new messages 
    sent via the chat form. When a POST request is received, it creates a new message in 
    the chat and returns the message as a JSON response. For GET requests, it retrieves 
    all messages associated with the chat and renders them in the chat template.

    Args:
        request (HttpRequest): The HttpRequest that contain metadata about the request method, 
        the text of the message, the author and the receiver

    Returns:
        JsonResponse: If the request method is POST, returns a JsonResponse containing the serialized 
                      data of the newly created message
        HttpResponse: If the request method is GET, returns an HttpResponse object that renders the 
                      chat template with the list of messages
    """
    myChat = Chat.objects.get(id = 1)
    if request.method == 'POST':
        message = request.POST['textmessage']
        new_message =  Message.objects.create(text = message, chat = myChat, author = request.user, receiver = request.user )
        serialized_obj = serialize('json', [new_message, ])
        return JsonResponse(serialized_obj[1:-1], safe = False)
    chatMessages = Message.objects.filter(chat__id = 1)
    return render(request, 'chat/chat.html', {'messages' : chatMessages})


def loginView(request):
    """ This view handles the login process of an existing user. It receives a POST request with 
    the username and password submitted via the login form. Thanks the function authenticate, 
    it check if the user exist. If the user exist it make the login and return a JsonResponse with a 
    status "success" and with the url for the access to the chat.html template. Otherwise, if the user do not exist, 
    it return a status "error 401". If the request method is GET it return a request object to render the 
    login.html template

    Args:
        request (HttpRequest): The HttpRequest object that contain metadata about the request method and the logged
        in user: username and password 

    Returns:
        JsonRepsonse: A JSON response indicating success or failure of the login attempt. If the authentication
                      succesful, it return a JsonResponse with the status "success" and the url for the access to 
                      the chat.html template. If the authrntication fail, it returns an error status with HTTP 401 
                      Unauthorize.
        HttpResponse: If the request method is GET, it returns an HttpResponse object rendering the login form, 
                      with the option to redirect after a successful login
        
    """
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
    """ This view handles the registration process for a new user. It receives a POST request with 
    the username, email, and password from the registration form in the register.html template.
    If the request method is POST, it creates a new user object, marks the user as staff, saves it, 
    and returns a JSON response with the URL to access the chat page. If the request method is not POST, 
    it renders the registration form.

    Args:
        request (HttpRequest): The HTTP request object that containt metadata about the request, in this case POST,
        the username, the email and password;

    Returns:
        JsonResponse: A JSON response with a status indicating success and the URL for accessing the chat page 
                      when a user is successfully created
        HTTPResponse: If the request method is not POST, it returns an HttpResponse object rendering the register.html
        template
    """
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST.get("username"), email = request.POST.get("email"), password = request.POST.get("password"))
        user.is_staff = True
        user.save()
        return JsonResponse({'status': 'success', 'url': '/chat/'})
    return render(request, 'auth/register.html')