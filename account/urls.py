from django.urls import path


from . import views
from .forms import UserEditForm

app_name = 'account'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.EditView.as_view(), name='edit'),
    path('password/', views.PasswordView.as_view(), name='password'),
]
