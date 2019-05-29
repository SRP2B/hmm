from django.db import models
from django.utils import timezone


# Create your models here.

class Nauczyciel(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    id_przedmiotu = models.ForeignKey('Przedmiot', on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwisko


class Sprawdzian(models.Model):
    id_nauczyciela = models.ForeignKey('Nauczyciel', on_delete=models.CASCADE)
    id_przedmiotu = models.ForeignKey('Przedmiot', on_delete=models.CASCADE)
    klasa = models.CharField(max_length=5, blank=True)
    title = models.CharField(max_length=120)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Przedmiot(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

