from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from account.models import User
from account.forms import LoginForm, AdvisorRegisterForm, SeekerRegisterForm

class MainLoginView(LoginView):
    template_name = 'signin.html'
    form_class = LoginForm

class RegisterView(TemplateView):
    template_name = 'registration.html'

class AdvisorView(CreateView):
    model = User
    template_name = 'financial-advisor.html'
    form_class = AdvisorRegisterForm
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        form.instance.is_advisor = True
        form.save()
        return super().form_valid(form)

class SeekerView(CreateView):
    model = User
    template_name = 'advice-seekers.html'
    form_class = SeekerRegisterForm
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        form.instance.is_seeker = True
        form.save()
        return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = 'profile.html'