from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Use your custom model

class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=True, label="Full Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label="Email Address", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser  # Ensure using CustomUser, not default User
        fields = ["name", "email", "password1", "password2"]

    def clean_email(self):
        """Ensure email is unique."""
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        """Save user with hashed password."""
        user = super().save(commit=False)
        user.name = self.cleaned_data["name"]  # Save name properly
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
