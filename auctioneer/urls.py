from django.urls import path
from . import views

app_name = 'auctioneer'

urlpatterns = [
    path('login/',views.login,name='auctioneer_login'),
]

