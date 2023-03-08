from datetime import datetime 
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.views import LoginView, LogoutView


class LoginInterfaceView(LoginView):
   template_name = 'home/login.html'

# Create your views here.
class HomeView(TemplateView):
   template_name = 'home/index.html'
   extra_context = {"time": datetime.today()}

class AuthorizedView(LoginRequiredMixin,TemplateView):
   template_name = "home/authorized.html"
   login_url = "/admin"
