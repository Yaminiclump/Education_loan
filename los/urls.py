from django.urls import path

from . import views

urlpatterns = [
    path('customer/create', views.customer_create, name='customer_create'),
    path('customer/update', views.customer_update, name='customer_update'),
    path('customer/contact/create', views.customer_contact, name='customer_contact'),
    path('customer/contact/update', views.update_contact, name='update_contact'),
    path('education/create', views.education_create , name='education_create'),
    path('education/update', views.education_update, name='education_update'),
    path('employment/create', views.create_empolyment, name='create_empolyment'),
    path('employment/update', views.update_empolyment, name='update_empolyment'),

]