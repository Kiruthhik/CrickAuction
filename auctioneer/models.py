# from django.db import models
# from players.models import PlayerProfile
# from franchise.models import FranchiseProfile
# # Create your models here.




    
# class AuctionFranchise(models.Model):
#     #auction = models.ForeignKey(LiveAuction, on_delete=models.CASCADE, related_name='auction_franchises')
#     original_franchise = models.ForeignKey(FranchiseProfile, on_delete=models.CASCADE, related_name='auction_entries')
#     purse = models.DecimalField(max_digits=30, decimal_places=0, null=True)

#     def __str__(self):
#         return f'{self.original_franchise.user.username} in {self.bidding_in.name}'

# class AuctionPlayer(models.Model):
#     #auction = models.ForeignKey(LiveAuction, on_delete=models.CASCADE , related_name='auction_players')
#     original_profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE, related_name='auction_entries')
#     bid = models.DecimalField(max_digits=15 ,decimal_places=0,  null=True)
#     team = models.CharField(max_length=20, default=None, null=True)
#     interested_team = models.ManyToManyField(AuctionFranchise,blank=True, related_name="interested_in")

#     def __str__(self):
#         return f'{self.original_profile.user.username} in {self.participating_in.name}'
    
# class LiveAuction(models.Model):
#     name = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     scheduled_time = models.DateTimeField()
#     auction_players = models.ManyToManyField(AuctionPlayer,on_delete=models.CASCADE,related_name="participating_in",blank=True)
#     auction_franchises = models.ManyToManyField(AuctionFranchise,on_delete=models.CASCADE,related_name="bidding_in",blank=True)
#     current_player = models.ForeignKey(AuctionPlayer,on_delete=models.CASCADE,null=True)
#     current_team_bid = models.ForeignKey(AuctionFranchise,on_delete=models.CASCADE,null=True)
#     leading_bidder = models.ForeignKey(AuctionFranchise,on_delete=models.CASCADE,null=True)
#     def __str__(self):
#         return f'{self.name} scheduled {self.scheduled_time}'

from django.db import models
from players.models import PlayerProfile
from franchise.models import FranchiseProfile


class AuctionFranchise(models.Model):
    original_franchise = models.ForeignKey(
        FranchiseProfile, on_delete=models.CASCADE, related_name="auction_entries"
    )
    purse = models.DecimalField(max_digits=30, decimal_places=0, default=0)

    def __str__(self):
        return f'{self.original_franchise.user.username}'


class AuctionPlayer(models.Model):
    original_profile = models.ForeignKey(
        PlayerProfile, on_delete=models.CASCADE, related_name="auction_entries"
    )
    bid = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    team = models.CharField(max_length=20, default=None, null=True, blank=True)
    interested_team = models.ManyToManyField(
        AuctionFranchise, blank=True, related_name="interested_in"
    )

    def __str__(self):
        return f'{self.original_profile.user.username}'


class LiveAuction(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField()
    auction_players = models.ManyToManyField(
        AuctionPlayer, related_name="auctions_participated_in", blank=True
    )
    auction_franchises = models.ManyToManyField(
        AuctionFranchise, related_name="auctions_bidding_for", blank=True
    )
    current_player = models.ForeignKey(
        AuctionPlayer, on_delete=models.CASCADE, null=True, blank=True, related_name="current_in"
    )
    current_team_bid = models.ForeignKey(
        AuctionFranchise, on_delete=models.CASCADE, null=True, blank=True, related_name="current_team_bid_in"
    )
    leading_bidder = models.ForeignKey(
        AuctionFranchise, on_delete=models.CASCADE, null=True, blank=True, related_name="leading_bidder_in"
    )

    def __str__(self):
        return f'{self.name} scheduled {self.scheduled_time}'
