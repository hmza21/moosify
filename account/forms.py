from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField, HiddenInput
from django.contrib.auth.forms import UserChangeForm, UsernameField, PasswordChangeForm

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    username = UsernameField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    
    first_name = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    
    last_name = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    
    email = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    
    password = None
    
class PasswordEditForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
    
    old_password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Old Password'
    }))
    
    new_password1 = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'New Password'
    }))
    
    new_password2 = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm New Password'
    }))