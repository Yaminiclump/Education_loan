from django.urls import path

from . import views

urlpatterns = [
    path('customer/create', views.customer_create, name='customer_create'),
    path('customer/update', views.customer_update, name='customer_update'),
    path('customer/contact/create', views.customer_contact_create, name='customer_contact_create'),
    path('customer/contact/update', views.customer_contact_update, name='customer_contact_update'),
    path('education/create', views.education_create , name='education_create'),
    path('education/update', views.education_update, name='education_update'),
    path('employment/create', views.employment_create, name='employment_create'),
    path('employment/update', views.employment_update, name='employment_update'),

]