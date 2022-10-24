from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from registration.forms import RegistrationForm

from registration.models import User


# Create your views here.

class IndexView(View):
    template = 'hubhu/index.html'

    def get(self, request):
        return render(request, self.template)


class LoginView(View):
    template = 'hubhu/login.html'

    def get(self,request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(pk = username)
            if user.password == password:
                request.session['user_id'] = user.username

        except:
            user = None
            print('unsucessful login')
        return render(request, self.template, {'msg' : True})

class RegistrationView(View):
    template = 'registration/register.html'

