from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.contrib.auth.models import User


class Category(models.Model):
    # Категория
    name = models.CharField('Категория', max_length=250)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Department(models.Model):
    # Категория
    name = models.CharField('Подразделение', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Task(models.Model):
    department = models.ForeignKey(
        User, verbose_name='Имя автора', on_delete=models.CASCADE)
    description = models.TextField('Описание')
    initiator = models.CharField('Инициатор', max_length=250)
    performer = models.CharField(
        'Исполнитель', max_length=250, blank=True, null=True, default='',)
    phone_number = models.CharField('Номер телефона', max_length=250)
    date_completed = models.DateTimeField(
        'Дата завершения', auto_now=False, blank=True, null=True)
    date_created = models.DateTimeField('Дата создания', auto_now_add=True,)
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE, null=True)
    completed = models.BooleanField('Завершить', default=False)

    def __str__(self):
        return str(self.department)

    def get_absolute_url(self):
        return reverse('tasks')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
