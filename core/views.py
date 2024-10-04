from django.views import View
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

def index(request: WSGIRequest):
    return render(request, 'core/index.html')

class RequestView(View):
    def get(self, request: WSGIRequest):
        return render(request, 'core/request.html')
