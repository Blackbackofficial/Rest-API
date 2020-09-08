from django.db import models


# Create your models here.

class Person(models.Model):
    title = models.CharField('Имя', max_length=30)
    person = models.TextField('Описание')

    def __str__(self):
        return self.person

    class Meta:  # Класс для переименовки названия таблички
        verbose_name = 'Человек'  # Единственное число
        verbose_name_plural = 'Люди'  # Множественное число
