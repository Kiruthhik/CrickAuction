from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import *
from players.models import PlayerProfile
from franchise.models import FranchiseProfile
from django.http import JsonResponse
# Create your views here.

def login(request):
    if request.method == "POST":
        auctioneer = request.POST.get('username')
        if(auctioneer == "auctioneer"):
            password = request.POST.get('password')
            user = authenticate(request,username = auctioneer, password = password)
            if user is not None:
                auth_login(request,user)
                messages.success(request,"successfull login")
                return redirect('auctioneer:auctioneer_index')
            else:
                messages.error(request,"wrong password")
        else:
            messages.error(request,"wrong username")
    return render(request,'auctioneer_login.html')

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        time = request.POST.get('time')
        LiveAuction.objects.create(name = name, scheduled_time = time).save
        return redirect('auctioneer:add',auc_name=name)

    return render(request,'auctioneer_index.html')

def add(request,auc_name):
    auction = LiveAuction.objects.get(name=auc_name)
    if request.method == 'POST':
        import json
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        type = data.get('type')
        try:
            if type == 'franchise':
                franchise = FranchiseProfile.objects.get(user__username=name)
                purse = data.get('purse')
                AuctionFranchise.objects.create(auction=auction,original_franchise=franchise,purse=purse).save
            elif type == 'player':
                player = PlayerProfile.objects.get(user__first_name=name)
                auc_player = AuctionPlayer.objects.create(auction=auction,original_profile=player)
                teams = list(AuctionFranchise.objects.filter(auction=auction))
                for team in teams:
                    auc_player.interested_team.add(team)
            return JsonResponse({'success': True, 'message': f'{type} {name} added successfully.'})
        
        except FranchiseProfile.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Franchise not found.'})
        
        except PlayerProfile.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Player not found.'})
    franchises = list(FranchiseProfile.objects.all())
    players = list(PlayerProfile.objects.all())
    content = {
        'players':players,
        'franchises':franchises,
        'name': auc_name
    }
    return render(request,'add.html',content)
