"""whitley_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.http import Http404
from django.urls import path, re_path
from django.shortcuts import render_to_response
from shop import models


def load_landing(request):
    return render_to_response("laning_page.html")

def load_store(request):
    d = {
        "shop": models.Shop_Item.objects.all()
    }
    return render_to_response("store_page.html", d)

def load_product_page(request, product_id):
    valid_urls = models.Shop_Item.objects.values_list("product_url", flat=True)
    if product_id in valid_urls:
        d = {"item": models.Shop_Item.objects.filter(product_url= product_id)}
        return render_to_response("product_page.html", d)
    else:
        raise Http404

def load_about_me(request):
    return render_to_response("about_me.html")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', load_landing),
    path("", load_landing),
    path("store", load_store),
    re_path("store/(\S+)", load_product_page),
    path('about', load_about_me)
]
