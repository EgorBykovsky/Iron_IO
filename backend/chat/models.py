from django.db import models

from session.models import Session
from users.models import User

# Chat model

class Chat(models.Model):
    """Модель чата"""
    Session = models.ForeignKey(Session, verbose_name="Игровая сессия чата", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
   
       