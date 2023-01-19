from django.contrib import admin
from django.urls import path, include

from python_34650.views import index


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
]
