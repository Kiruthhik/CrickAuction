from django.shortcuts import render,redirect
from .models import PlayerProfile
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['useremail']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            if user.groups.filter(name='players').exists():
                login(user)
                return redirect()
            else:
                messages.warning(request,"login with player credentials")
        else:
            messages.warning(request,"wrong credentials")

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        print("successful post")
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        email = request.POST['email']
        contact = request.POST['contact']
        native = request.POST['native']
        role = request.POST['role']
        batting_style = request.POST['Batting style']
        bowling_style = request.POST['Bowling style']
        dob = request.POST['dob']
        base_price = request.POST['base price']
        #username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confpassword']
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('players:player_register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use in User model.")
            return redirect('players:player_register')
        
        user = User.objects.create_user(username=email, password=password, email=email, first_name=FirstName, last_name=LastName)
        
        # Create PlayerProfile associated with the user
        player_profile = PlayerProfile.objects.create(
            user=user,
            contact_number=contact,
            native=native,
            role=role,
            batting_style=batting_style,
            bowling_style=bowling_style,
            dob=dob,
            base_price=base_price
        )
        #player_profile.save()
        
        # Add user to the players group
        player_group = Group.objects.get(name='players')
        user.groups.add(player_group)
        
        messages.success(request, "Registration successful.")
        return redirect('players:player_login')  # Assuming you have a login view
    return render(request,'register.html')