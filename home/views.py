from datetime import datetime 
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

class SignupView(CreateView):
   form_class = UserCreationForm
   template_name = 'home/register.html'
   success_url = '/smart/notes'

   def get(self, request, *args, **kwargs):
       if self.request.user.is_authenticated:
           return redirect('notes.list')
       return super().get(request, *args, **kwargs)
   
   def form_valid(self, form):
      response = super().form_valid(form)
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(self.request, user)
      return response

class LogoutInterfaceView(LogoutView):
   template_name = 'home/logout.html'
class LoginInterfaceView(LoginView):
   template_name = 'home/login.html'

# Create your views here.
class HomeView(TemplateView):
   template_name = 'home/index.html'
   extra_context = {"time": datetime.today()}

class AuthorizedView(LoginRequiredMixin,TemplateView):
   template_name = "home/authorized.html"
   login_url = "/admin"
