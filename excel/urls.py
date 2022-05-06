from django.urls import path
from . import views

urlpatterns = [
    path('add_excel_file/', views.add_excel_file, name='add_excel_file'),
    path('', views.home),
    path('client_summary', views.client_summary),
    path('clients', views.clients_list)
]
