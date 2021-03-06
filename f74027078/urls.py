"""f74027078 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.http import HttpResponse
from world import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.display_form),
	url(r'^index/', views.display_form),
    url(r'^data/', views.get_serealize, name='data',),
	url(r'^data/(?P<country_id>\w{4})(?P<display_mode>\w{4})/$', views.get_serealize, name='data',),
    url(r'^display/', TemplateView.as_view(template_name='./world/leaflet_template.html'),name='home'),	
]
