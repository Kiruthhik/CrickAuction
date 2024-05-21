from django.urls import path
from . import views

app_name = 'franchise'

urlpatterns = [
    path('login/',views.login,name='franchise_login'),
    path('register/',views.register,name='franchise_register'),
    path('dashboard/',views.dashboard,name='franchise_dashboard'),

]

