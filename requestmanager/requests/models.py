from django.db import models

# Create your models here.
# Создайте модель заявки
# В файле requests/models.py создайте модель Request с полями:

# name — имя пользователя (строка до 100 символов).
# email — email пользователя.
# message — сообщение от пользователя (текстовое поле).
# submitted_at — дата и время подачи заявки.


class Request(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100, unique=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ': ' + self.message[:10] + '...'