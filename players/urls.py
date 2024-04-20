from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('login/',views.login,name='player_login'),
    path('register/',views.register,name='player_register'),
]

