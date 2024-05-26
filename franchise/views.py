from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import FranchiseProfile
from players.models import PlayerProfile
from django.shortcuts import render, get_object_or_404

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            if user.groups.filter(name='franchise').exists():
                auth_login(request,user)
                messages.success(request,"login successfull")
                return redirect('franchise:dashboard1')
            else:
                messages.warning(request,"login with franchise credentials")
        

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

def dashboard(request):
    players = list(PlayerProfile.objects.all())
    return render(request,'franchise_dashboard.html',{'players':players})

@login_required
def bid(request,player_email):
     player = get_object_or_404(PlayerProfile, user__email=player_email)

     if request.method == 'POST':
        user = request.user
        if user.groups.filter(name='franchise').exists():

            bid = int(request.POST['bid']) 
            if player.current_bid is None and bid >= player.base_price:
                player.current_bid = bid
                player.current_team = request.user.username
                player.save()
                messages.success(request,"bid successfull")
                return redirect('franchise:franchise_dashboard')


            elif(bid > player.current_bid):
                last_bid = player.current_bid
                last_team = player.current_team
                franchise = get_object_or_404(FranchiseProfile, user__username = last_team)
                franchise.purse_money = franchise.purse_money + last_bid
                franchise.save()
                player.current_bid = bid
                player.current_team = request.user.username
                player.save()
                franchise1 = get_object_or_404(FranchiseProfile, user = request.user)
                franchise1.purse_money = franchise1.purse_money - bid
                franchise1.save()
                messages.success(request,"bid successfull")
                return redirect('franchise:franchise_dashboard')

            
            else:
                messages.warning(request,"bid failed")
        
        else:
            messages.warning(request,"you don't have access")
            
            return redirect('franchise:franchise_dashboard')
     return render(request,'bid.html',{'player_data':player})

@login_required
def dashboard1(request):
    franchise_user = request.user
    franchise_data = get_object_or_404(FranchiseProfile, user=franchise_user)
    players = list(PlayerProfile.objects.filter(current_team = franchise_user.username))
    context = {
        'players': players,
        'franchise': franchise_data
    }
    return render(request,'dashboard.html',context)