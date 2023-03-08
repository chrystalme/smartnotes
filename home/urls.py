from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view()),
    path('login', views.LoginInterfaceView.as_view()),
]
