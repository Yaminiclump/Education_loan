from django.urls import path
from . import views

urlpatterns = [
    path('customer/create', views.customer_create, name='customer_create'),
    path('customer/update', views.customer_update, name='customer_update'),
    path('customer/contact', views.customer_contact, name='customer_contact'),
]