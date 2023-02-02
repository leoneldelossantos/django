from django.contrib import admin
from django.urls import path, include

from python_34650.views import index, about


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
    path('users/', include('users.urls')),
    path('about/', about,  name='about'),
]
