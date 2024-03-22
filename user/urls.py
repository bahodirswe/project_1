from django.urls import path
from . import views


app_name = "user"

urlpatterns = [
    path('sign-up/', views.sign_up, name="sign_up"),
    path('sign-in/', views.LoginView.as_view(), name="sign_in"),
]
