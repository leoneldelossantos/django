from django.contrib import admin

from contacts.models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone_number','is_active')

