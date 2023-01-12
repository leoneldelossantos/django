from django.urls import path
from contacts.views import contacts_list, create_contact

urlpatterns = [
    path('contacts-list/', contacts_list, name='contacts_list'),
    path('contacts-create/', create_contact, name='contacts_create'),

]