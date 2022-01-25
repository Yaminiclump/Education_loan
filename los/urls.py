from django.urls import path
from . import views

urlpatterns = [
    path('customer/create', views.customer_create, name='customer_create'),
]