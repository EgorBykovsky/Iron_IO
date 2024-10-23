from django.db import models

# Create your models here.

class User(models.Model):
    """user model"""    
    session = models.ForeignKey('session.Session', on_delete=models.CASCADE)
    score = models.IntegerField("Баллы", default=0)
    name = models.CharField("Никнейм", max_length=100)
    
    