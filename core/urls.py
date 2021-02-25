from django.urls import path

from .views import (
    HomePageView,
    CongratulationsPageView,
    MatchedView,
    MessageAdvisorView
)

app_name = 'core'


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("congratulations/", CongratulationsPageView.as_view(), name="congratulations"),
    path("matched-advisors/", MatchedView.as_view(), name="matched-advisors"),
    path("message-advisor/<slug:slug>", MessageAdvisorView.as_view(), name="message-advisor"),
]