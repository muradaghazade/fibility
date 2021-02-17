from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class MainLoginView(LoginView):
    template_name = 'signin.html'

class RegisterView(TemplateView):
    template_name = 'registration.html'

class AdvisorView(TemplateView):
    template_name = 'financial-advisor.html'

class SeekerView(TemplateView):
    template_name = 'advice-seekers.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'