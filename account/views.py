from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from account.models import User
from account.forms import LoginForm, AdvisorRegisterForm, SeekerRegisterForm, UpdateProfileForm
from django.core.exceptions import PermissionDenied

class MainLoginView(LoginView):
    template_name = 'signin.html'
    form_class = LoginForm

class RegisterView(TemplateView):
    template_name = 'registration.html'

class AdvisorView(CreateView):
    model = User
    template_name = 'financial-advisor.html'
    form_class = AdvisorRegisterForm
    success_url = reverse_lazy('core:congratulations')

    def form_valid(self, form):
        form.instance.is_advisor = True
        form.save()
        return super().form_valid(form)

class SeekerView(CreateView):
    model = User
    template_name = 'advice-seekers.html'
    form_class = SeekerRegisterForm
    success_url = reverse_lazy('core:congratulations')

    def form_valid(self, form):
        form.instance.is_seeker = True
        form.save()
        return super().form_valid(form)    

class ProfileView(UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('core:index')

    # def get_success_url(self):
    #     return reverse_lazy('accounts:user-profile', kwargs={'pk':self.get_object().pk})

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.username != self.get_object().username:
            raise PermissionDenied
        return super(ProfileView, self).dispatch(request, *args, **kwargs)