from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import AboutUsText, MoreOnUsText

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutus'] = AboutUsText.objects.order_by('-id').first
        context['moreonus'] = MoreOnUsText.objects.order_by('-id').first
        return context



class CongratulationsPageView(TemplateView):
    template_name = 'congratulation.html'