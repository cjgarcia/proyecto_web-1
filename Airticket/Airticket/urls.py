"""Airticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from registro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('reservar/', views.reservar, name='reservar'),
    path('reservar/clientes/', views.clientes_view, name='clientes_view'),
    path('reservar/clientes/edit/<int:id_cliente>', views.clientes_edit, name='clientes_edit'),
    path('reservar/clientes/update/<int:id_cliente>', views.clientes_update, name='clientes_update'),
    path('reservar/clientes/delete/<int:id_cliente>', views.clientes_delete, name='clientes_delete'),
    path('contac/', views.contac, name='contac'),
    path('vuelos/', views.vuelo, name='vuelo'),
    path('vuelos/listado/', views.vuelo_view, name='vuelo_view'),
    path('vuelos/edit/<int:id_vuelo>', views.vuelo_edit, name='vuelo_edit'),
    path('vuelos/update/<int:id_vuelo>', views.vuelo_update, name='vuelo_update'),
    path('vuelos/delete/<int:id_vuelo>', views.vuelo_delete, name='vuelo_delete'),
    
]
