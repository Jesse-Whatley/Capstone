from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.user.username