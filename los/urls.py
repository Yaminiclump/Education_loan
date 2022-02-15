from django.urls import path

from . import views

urlpatterns = [
    path('customer/create', views.customer_create, name='customer_create'),
    path('customer/update', views.customer_update, name='customer_update'),
    path('customer/contact/create', views.customer_contact, name='customer_contact'),
    path('education/create', views.create_education_service , name='customer_education_create'),
    path('education/update', views.update_education, name='update_education'),
    path('customer/contact/update', views.update_contact, name='update_contact'),
]