from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField('Имя', max_length=20, blank=False, help_text="Enter field name")
    age = models.IntegerField('Возраст', null=True)
    address = models.CharField('Адресс', max_length=20, default='')
    work = models.CharField('Работа', max_length=20, default='')

    def __str__(self):
        return self.name

    class Meta:  # Класс для переименовки названия таблички
        verbose_name = 'Человек'  # Единственное число
        verbose_name_plural = 'Люди'  # Множественное число
        ordering = ["id"]  # Сортировка по имени
