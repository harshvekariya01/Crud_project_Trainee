from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
class leave(models.Model):
    user = models.EmailField( null=True,editable=False)
    start_date = models.DateField()
    end_date = models.DateField()     
    remaining_leave = models.IntegerField(null=True)
    reason = models.TextField() 
    approved  = models.BooleanField(default=False)  