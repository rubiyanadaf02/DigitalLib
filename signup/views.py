from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create user but don't save yet
            user.set_password(form.cleaned_data["password1"])  # Hash password
            user.is_active = True  # Ensure the user can log in
            user.save()

            login(request, user)  # Log in the user after registration
            return redirect("homepage")  # Ensure "home" URL exists or change to "/"
    else:
        form = UserRegistrationForm()

    return render(request, "signup.html", {"form": form})
