from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from account.views import MainLoginView,RegisterView,AdvisorView,SeekerView,ProfileView

app_name = 'account'

urlpatterns = [
    path('login/', MainLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register-advisor/', AdvisorView.as_view(), name='advisor'),
    path('register-seeker/', SeekerView.as_view(), name='seeker'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('log-out', LogoutView.as_view(), name='log-out'),
]