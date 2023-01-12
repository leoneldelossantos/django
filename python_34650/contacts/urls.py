from django.urls import path
from contacts.views import contacts_list, contacts_create

urlpatterns = [
    path('contacts-list/', contacts_list, name='contacts_list'),
    path('contacts-create/', contacts_create, name='contacts_create'),

]