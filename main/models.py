from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField('Имя', max_length=20, help_text="Enter field name")
    age = models.IntegerField('Возраст', help_text="Enter field age", blank=False, default="")
    address = models.CharField('Адресс', max_length=20, help_text="Enter field address", blank=False, default="")
    work = models.CharField('Работа', max_length=20, help_text="Enter field address", blank=False, default="")

    def __str__(self):
        return self.name

    class Meta:  # Класс для переименовки названия таблички
        verbose_name = 'Человек'  # Единственное число
        verbose_name_plural = 'Люди'  # Множественное число
        ordering = ["-name"]  # Сортировка по имени
