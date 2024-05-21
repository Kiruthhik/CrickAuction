# players/models.py

from django.contrib.auth.models import User
from django.db import models

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    '''first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)'''
    contact_number = models.CharField(max_length=15)
    native = models.CharField(max_length=10, choices=[('Indian', 'Indian'), ('overseas', 'Overseas')])
    role = models.CharField(max_length=20, choices=[('Batter', 'Batter'), ('Bowler', 'Bowler'), ('all_rounder', 'All rounder')])
    batting_style = models.CharField(max_length=20, choices=[('right handed', 'Right handed'), ('left handed', 'Left handed'), ('NULL', 'None')])
    bowling_style = models.CharField(max_length=20, choices=[('right arm fast', 'Right arm fast'), ('right arm medium', 'Right arm medium'), ('right arm spin', 'Right arm spin'), ('left arm fast', 'Left arm fast'), ('left arm medium', 'Left arm medium'), ('left arm spin', 'Left arm spin'), ('NULL', 'None')])
    dob = models.DateField()
    base_price = models.DecimalField(max_digits=15, decimal_places=2)
    current_team = models.CharField(max_length=20,default=None,null=True)
    current_bid = models.DecimalField(max_digits=15,decimal_places=0,default=None,null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
