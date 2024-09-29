from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserEditForm, PasswordEditForm

def index(request: WSGIRequest):
    return render(request, 'account/index.html')

class EditView(LoginRequiredMixin, View):
    
    def get(self, request: WSGIRequest):
        
        context = {
            'form': UserEditForm(instance=request.user)
        }
        
        return render(request, 'account/edit.html', context)
    
    def post(self, request: WSGIRequest):
    
        form = UserEditForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('account:index')
        else:
            return redirect('account:edit')

class PasswordView(LoginRequiredMixin, View):
    
    def get(self, request: WSGIRequest):
        
        context = {
            'form': PasswordEditForm(user=request.user)
        }
        
        return render(request, 'account/password.html', context)
    
    def post(self, request: WSGIRequest):
    
        form = PasswordEditForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('account:index')
        else:
            return redirect('account:password')