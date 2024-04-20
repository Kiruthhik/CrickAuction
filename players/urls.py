from django.urls import path
from . import views

urlpatterns = [
    path('',views.layout,name='layout'),
]

