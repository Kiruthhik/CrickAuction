from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

def index(request):
    return render(request,'index.html')
    #return HttpResponse("hello, welcome to index page")

def user_logout(request):
    logout(request)
    return render(request,'index.html')

