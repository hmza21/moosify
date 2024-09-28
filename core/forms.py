from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class UserLoginForm(AuthenticationForm):
    
    username = UsernameField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))