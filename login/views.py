from django.shortcuts import render
from .models import Login
# Create your views here.

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        Login.objects.create(
            email=email,
            password=password,
        )
    return render(request,'login.html') 
    

