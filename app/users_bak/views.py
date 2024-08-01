from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from .models import User

class AuthView(LoginView):
    template_name = 'users/login.html'