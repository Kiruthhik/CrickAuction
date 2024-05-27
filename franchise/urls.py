from django.urls import path
from . import views

app_name = 'franchise'

urlpatterns = [
    path('login/',views.login,name='franchise_login'),
    path('register/',views.register,name='franchise_register'),
    path('dashboard/',views.dashboard,name='franchise_dashboard'),
    path('bid/<str:player_email>',views.bid,name='bid'),
    path('dashboard1/',views.dashboard1,name='dashboard1'),
    path('report/',views.report,name = 'report'),
]

