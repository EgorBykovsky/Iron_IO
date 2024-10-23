from django.db import models

# Model of game session.

class Session(models.Model):
    """ Model of game session """
    session_id = models.BigIntegerField(
        "Идентификатор сессии",        
        editable=False, 
        unique=True,
        default = 0
        )
    creator = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE, 
        related_name='created_sessions'
        )
    word = models.CharField(max_length=200)