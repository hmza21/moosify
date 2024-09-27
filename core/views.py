from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest

from download.models import Track

def index(request: WSGIRequest):
    return render(request, 'core/index.html')