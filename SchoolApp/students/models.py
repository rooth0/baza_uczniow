'''
Zadanie zaliczeniowe z Django
Imię i nazwisko ucznia: Olaf Tojza
Data wykonania zadania: 25.03.2024 
Treść zadania: Baza uczniów dojeżdżających do szkoły
Opis funkcjonalności aplikacji: Aplikacja umożliwia dodawanie, przeglądanie, wyszukiwanie, sortowanie oraz usuwanie uczniów, którzy dojeżdżają do szkoły.
Użytkownik może dodawać nowych uczniów, wprowadzając ich dane, takie jak imię, nazwisko, miasto, dystans do szkoły i klasa.
Może również przeglądać listę wszystkich uczniów, wyszukiwać ich po imieniu lub nazwisku, sortować ich według różnych kryteriów, takich jak imię, nazwisko, miasto, dystans do szkoły lub klasa,
oraz usuwać niepotrzebne wpisy.
'''
from django.db import models

# Model reprezentujący studenta.
class Student(models.Model):
    first_name = models.CharField(max_length=100)  # Pole przechowujące imię studenta.
    last_name = models.CharField(max_length=100)  # Pole przechowujące nazwisko studenta.
    address = models.CharField(max_length=200)  # Pole przechowujące adres studenta.
    distance_to_school = models.FloatField()  # Pole przechowujące odległość do szkoły.
    school_class = models.IntegerField()  # Pole przechowujące klasę studenta.

    # Metoda zwracająca reprezentację tekstową obiektu.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
