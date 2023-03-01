from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('authorized', views.AuthorizedView.as_view(), name="authorized")
]
