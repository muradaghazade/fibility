from django.shortcuts import render, redirect
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'index.html'


class CongratulationsPageView(TemplateView):
    template_name = 'congratulation.html'