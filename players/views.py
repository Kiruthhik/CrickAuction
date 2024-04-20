from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def layout(request):
    #return HttpResponse("hello world")
    return render(request,'layout.html')