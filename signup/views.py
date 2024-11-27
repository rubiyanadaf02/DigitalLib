from django.shortcuts import render
from .models import Signup
# Create your views here.

def signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpass=request.POST.get('cpass')

        Signup.objects.create(
            name=name,
            email=email,
            password=password,
            cpass=cpass,
        )
    return render(request,'signup.html')    

