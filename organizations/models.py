from django.db import models
from base.models import Cities

class Organizations(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=12)
    company_url = models.URLField(max_length=250)
    address = models.CharField(max_length=150, null=True, blank=True)
    location = models.ForeignKey(Cities, on_delete=models.CASCADE, default="")
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
        