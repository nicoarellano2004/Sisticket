from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    rut = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='usuarios/%Y/%m/%d', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        super().save(*args, **kwargs)