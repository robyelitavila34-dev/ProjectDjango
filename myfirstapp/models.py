from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    state = models.BooleanField(default=True)
    
    