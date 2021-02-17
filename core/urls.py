from django.urls import path

from .views import (
    HomePageView,
    CongratulationsPageView,
)

app_name = 'core'


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("congratulations/", CongratulationsPageView.as_view(), name="congratulations")
]