from django.urls import path
from .views import HomePageView
from .views import AboutView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about', AboutView.as_view(), name = 'about')
]