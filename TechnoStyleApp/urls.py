"""
URL configuration for technostyle project.

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
from django.urls import path
from TechnoStyleApp import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_producto/',views.agregar_producto, name='agregar-productos'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar_sucursal/', views.agregar_sucursal, name='agregar_sucursal'),
    path('buscar/',views.buscar_productos, name='buscar_productos')
    
]
