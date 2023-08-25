"""
URL configuration for SpaceX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from SpaceX_Shopping import views

urlpatterns = [
    path ('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('mens_shirt',views.mens_shirt,name='mens_shirt'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('shirt1',views.shirt1,name='shirt1'),
    path('shirt2',views.shirt2,name='shirt2'),
    path('cart_view',views.cart_view,name='cart_view'),
    path('remove_from_cart', views.remove_from_cart, name='remove_from_cart'),
    # path('remove_from_cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('remove_from_cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    
]
