from django.db import models
from django.contrib.auth.models import User

class DatosExtras(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.CharField( max_length=100)
    avatar = models.ImageField(upload_to='avatares',null=True,blank=True)