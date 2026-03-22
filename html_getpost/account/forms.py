from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password=cleaned_data.get("password")
        self.user=authenticate(username=username, password=password)
        if not self.user:
            raise forms.ValidationError("Invalid username or password")
        return cleaned_data