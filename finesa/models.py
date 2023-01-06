from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
 users = models.ForeignKey(User, on_delete=models.CASCADE)
 empresa = models.CharField(max_length=50)
 content= models.TextField()
 def __str__(self):
  return self.empresa


