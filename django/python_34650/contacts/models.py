from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name} - {self.email}' 
