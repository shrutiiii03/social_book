from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  
    public_visibility = models.BooleanField(default=True)
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    @property
    def age(self):
        if self.birth_year:
            from datetime import date
            return date.today().year - self.birth_year
        return None

    def __str__(self):
        return self.email

class UploadedFile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    description = models.TextField()
    visibility = models.BooleanField(default=True) 
    cost = models.DecimalField(max_digits=6, decimal_places=2) 
    year_of_publication = models.IntegerField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True) 

    def __str__(self):
        return self.title
