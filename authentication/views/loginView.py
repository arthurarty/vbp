from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from authentication.models import User
from authentication.forms.loginForm import LoginForm


class Login(LoginView):
    """
    Class to handle user login
    """
    template_name = 'authentication/login.html'
    authentication_form = LoginForm
    next = '/profile'


class Profile(View):
    """
    Handle profile view
    """
    def get(self, request):
        """
        return profile view
        """
        context = {
            'user': request.user
        }
        return render(request, 'authentication/profile.html', context)
