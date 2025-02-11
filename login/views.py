from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    error_message = None  # Initialize error message as None
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("homepage")  # Redirect to the homepage upon successful login
        else:
            error_message = "Invalid email or password. Please try again."

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form, "error_message": error_message})

