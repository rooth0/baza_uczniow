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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # Ścieżka do wyświetlenia listy studentów.
    path('add/', views.add_student, name='add_student'),  # Ścieżka do dodawania nowego studenta.
    path('sort_by_name/', views.sort_by_name, name='sort_by_name'),  # Ścieżka do sortowania studentów po imieniu.
    path('sort_by_last_name/', views.sort_by_last_name, name='sort_by_last_name'),  # Ścieżka do sortowania studentów po nazwisku.
    path('sort_by_address/', views.sort_by_address, name='sort_by_address'),  # Ścieżka do sortowania studentów po adresie.
    path('sort_by_class/', views.sort_by_class, name='sort_by_class'),  # Ścieżka do sortowania studentów po klasie.
    path('sort_by_distance/', views.sort_by_distance, name='sort_by_distance'),  # Ścieżka do sortowania studentów po odległości do szkoły.
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),  # Ścieżka do usuwania studenta.
]
