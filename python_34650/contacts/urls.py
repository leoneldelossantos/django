from django.urls import path
from contacts.views import contacts_list, create_contact, update_contact, ContactDeleteView

urlpatterns = [
    path('contacts-list/', contacts_list, name='contacts_list'),
    path('contacts-create/', create_contact, name='contacts_create'),
    path('update-contact/<int:pk>/', update_contact, name='update_contact'),
    path('delete-contact/<int:pk>/', ContactDeleteView.as_view(), name='delete_contact'),
]