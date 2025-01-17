from django.urls import path
from . import views

app_name = 'auctioneer'

urlpatterns = [
    path('login/',views.login,name='auctioneer_login'),
    path('index/',views.index,name="auctioneer_index"),
    path('live_auction/<str:auc_name>',views.live_auction,name="live_auction"),
    path('add/<str:auc_name>',views.add,name="add"),
    path('auction/<str:auc_name>',views.auction,name="auction"),
]