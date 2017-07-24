"""generateinvoice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
admin.autodiscover()
from serve.views import main,regenerate,login_x,logout_x

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',login_x),
    url(r'^generate/',main),
    url(r'^logout/',logout_x),
    url(r'^regenerate/',regenerate),
]
