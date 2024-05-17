from django.urls import path
from rest_framework import routers
from .api import UserViewSet

from . import views


app_name = "user"

urlpatterns = [
    path('registration/sign-up/', views.sign_up, name="sign_up"),
    path('registration/sign-in/', views.LoginView.as_view(), name="sign_in"),
    path('dashboard/<uuid:id>/', views.dashboard, name="dashboard"),
    path('profile/<uuid:id>/', views.profile, name='profile'),
    path('follow/<uuid:id>/', views.follow, name='follow'),
    path('followers/<uuid:id>/', views.follow_info, name='follow_info'), 
    path('logout/', views.user_logout, name='user_logout'),
]
