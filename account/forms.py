from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField, HiddenInput
from django.contrib.auth.forms import UserChangeForm, UsernameField, PasswordChangeForm

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    
    username = UsernameField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }), label='Username')
    
    email = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }), label='Email')
    
    password = None
    
class PasswordEditForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    
    old_password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Old password'
    }), label='Old Password')
    
    new_password1 = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'New password'
    }), label='New Password')
    
    new_password2 = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm new password'
    }), label='Confirm New Password')