from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    complete = models.BooleanField(default=False, verbose_name='Выполнено')
    favorite = models.BooleanField(default=False, verbose_name='Добавить в избранное')
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete', '-favorite']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

