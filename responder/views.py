from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from responder.models import User
@csrf_exempt
def index(request):


    if request.method == 'GET':
        login = request.GET.get('login', None)
        if login:
            user = User.objects.filter(login__iexact=login)[0]
            response = "For the login " + login + " the name is " + user.name + " and surname is " + user.surname
        else:
            response = 'Login necessary'
        return HttpResponse(response)


    if request.method == 'POST':
        login = request.POST.get('login', None)
        name = request.POST.get('name', None)
        surname = request.POST.get('surname', None)
        new_user = User()
        new_user.login = login
        new_user.name = name
        new_user.surname = surname
        new_user.save()
        return HttpResponse("User saved")


    else:
        return HttpResponse("Bad Request")
# Create your views here.
