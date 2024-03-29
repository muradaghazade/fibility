from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import AboutUsText, MoreOnUsText
from account.models import User
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import MessageForm

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutus'] = AboutUsText.objects.order_by('-id').first
        context['moreonus'] = MoreOnUsText.objects.order_by('-id').first
        return context

class MatchedView(ListView):
    model = User
    context_object_name = "matched_advisors"
    template_name = "table.html"
    queryset = User.objects.filter(is_advisor=True).order_by('-id')[:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def get_queryset(self):
        
    #     print(queryset)

    #     return queryset

class MessageAdvisorView(FormMixin, DetailView):
    model = User
    context_object_name = "advisor"
    template_name = "message.html"
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('core:message-congratulations')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.receiver = self.get_object()
        form.save()
        return super().form_valid(form)


class CongratulationsPageView(TemplateView):
    template_name = 'congratulation.html'


class MessageCongratulationsPageView(TemplateView):
    template_name = 'mcongratulation.html'