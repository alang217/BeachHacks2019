from django.conf.urls import url
from .views import HomeView, AboutView
from django.urls import path


urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('/about', AboutView.as_view(), name="about"),
]