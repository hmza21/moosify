from django.urls import path

from . import views

app_name = 'download'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('download/', views.DownloadView.as_view(), name='download'),
]