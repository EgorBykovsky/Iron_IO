from django.db import models
from session.models import Session
from users.models import User

# Create your models here.
class Message(models.Model):
    Session = models.ForeignKey(Session, verbose_name="Игровая сессия чата", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)