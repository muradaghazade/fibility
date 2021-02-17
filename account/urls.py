from django.contrib import admin
from django.urls import path, include
from account.views import MainLoginView,RegisterView,AdvisorView,SeekerView,ProfileView

app_name = 'account'

urlpatterns = [
    path('login/', MainLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register-advisor/', AdvisorView.as_view(), name='advisor'),
    path('register-seeker/', SeekerView.as_view(), name='seeker'),
    path('profile/', ProfileView.as_view(), name='seeker'),
]