"""
URL configuration for eisaal_foundation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('achievement', views.achievement, name='achievement'),
    path('nation_donation', views.national_donation, name='national_donation'),
    path('international_donation', views.international_donation, name='international_donation'),
    path('contact', views.contact, name='contact'),
    path('donationUpcomingProject', views.donationUpcomingProject, name='donationUpcomingProject'),
    # path('shop/', include('eisaal_shop.urls')),
]
