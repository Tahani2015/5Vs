"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()

import emotion_map.views

urlpatterns = [
    url(r'^$', emotion_map.views.index, name='index'),
    url(r'^index$', emotion_map.views.index, name='index'),
    url(r'^about$', emotion_map.views.about, name="about"),
    url(r'^US$', emotion_map.views.US, name="US"),
    url(r'^Australia$', emotion_map.views.Australia, name="Australia"),
    url(r'^UK$', emotion_map.views.UK, name="UK"),
    url(r'^db', emotion_map.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

]
