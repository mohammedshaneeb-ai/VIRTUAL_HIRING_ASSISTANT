from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('get/', views.chat, name='chat'),    
    path('export-csv/', views.export_csv, name='export_csv'),


]