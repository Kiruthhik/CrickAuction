from django.db import models
from players.models import PlayerProfile
from franchise.models import FranchiseProfile
# Create your models here.



class LiveAuction(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField()
    
    def __str__(self):
        return f'{self.name} scheduled {self.scheduled_time}'
    
class AuctionFranchise(models.Model):
    auction = models.ForeignKey(LiveAuction, on_delete=models.CASCADE, related_name='auction_franchises')
    original_franchise = models.ForeignKey(FranchiseProfile, on_delete=models.CASCADE, related_name='auction_entries')
    purse = models.DecimalField(max_digits=30, decimal_places=0, default=None, null=True)

    def __str__(self):
        return f'{self.auction.name} in {self.original_franchise.user.username}'

class AuctionPlayer(models.Model):
    auction = models.ForeignKey(LiveAuction, on_delete=models.CASCADE , related_name='auction_players')
    original_profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE, related_name='auction_entries')
    bid = models.DecimalField(max_digits=15 ,decimal_places=0, default=None , null=True)
    team = models.CharField(max_length=20, default=None, null=True)
    interested_team = models.ForeignKey(AuctionFranchise, on_delete=models.SET_NULL ,null=True,blank=True, related_name="interested_in")

    def __str__(self):
        return f'{self.original_profile.user.username in self.auction.name}'