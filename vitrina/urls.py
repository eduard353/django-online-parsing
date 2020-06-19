from django.contrib import admin
from django.urls import path, include
from . import views


app_name='vitrina'

urlpatterns = [
   path('', views.dashboard_view, name="dashboard"),
   path('parsers/', views.parsers_view, name="parsers"),
   path('data/', views.data_view, name="data"),
]
