from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import FranchiseProfile


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['useremail']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            if user.groups.filter(name='franchise').exists():
                login(user)
                return redirect()
            else:
                messages.warning(request,"login with franchise credentials")
        else:
            messages.warning(request,"wrong credentials")

    return render(request,'franchise_login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        lisence = request.POST['liscence']
        password = request.POST['password']
        confpassword = request.POST['confpassword']

        if password != confpassword:
            messages.error(request,"password and confirmation doesn't match")
            return redirect('franchise:franchise_register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use in User model.")
            return redirect('franchise:franchise_register')
        
        user = User.objects.create_user(username=username, email=email, password=password)

        franchise_object = FranchiseProfile.objects.create(user=user,liscence=lisence)

        franchise_group = Group.objects.get(name='franchise')
        user.groups.add(franchise_group)
        
        messages.success(request, "Registration successful.")
        return redirect('franchise:franchise_login')

        
    return render(request,'franchise_register.html')