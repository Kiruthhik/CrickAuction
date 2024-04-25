from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == 'POST':
        pass
    return render(request,'franchise_login.html')

def register(request):
    if request.method == 'POST':
        pass
    return render(request,'franchise_register.html')