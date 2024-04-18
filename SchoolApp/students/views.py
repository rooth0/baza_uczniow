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
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm, Student
import json
from django.db.models import Q

# Ta funkcja obsługuje żądanie wyświetlenia listy studentów.
def student_list(request):
    query = request.GET.get('query')
    sort_by = request.GET.get('sort_by')
    students = Student.objects.all()

    if query:
        query_parts = query.split(' ')
        first_name = query_parts[0]
        last_name = ' '.join(query_parts[1:]) if len(query_parts) > 1 else ''

        if last_name:
            students = students.filter(
                first_name__icontains=first_name,
                last_name__icontains=last_name
            )
        else:
            students = students.filter(
                Q(first_name__icontains=first_name) | Q(last_name__icontains=first_name)
            )

    if sort_by:
        students = students.order_by(sort_by)

    return render(request, 'students/student_list.html', {'students': students, 'query': query, 'sort_by': sort_by})

# Ta funkcja obsługuje żądanie dodania nowego studenta.
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            return render(request, 'students/add_student.html', {'form': form, 'error_message': 'Wszystkie pola muszą być wypełnione!'})
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})


# Ta funkcja sortuje listę studentów po imieniu.
def sort_by_name(request):
    students = Student.objects.order_by('first_name')
    return render(request, 'students/student_list.html', {'students': students})

# Ta funkcja sortuje listę studentów po nazwisku.
def sort_by_last_name(request):
    students = Student.objects.order_by('last_name')
    return render(request, 'students/student_list.html', {'students': students})

# Ta funkcja sortuje listę studentów po adresie.
def sort_by_address(request):
    students = Student.objects.order_by('address')
    return render(request, 'students/student_list.html', {'students': students})

# Ta funkcja sortuje listę studentów po klasie.
def sort_by_class(request):
    students = Student.objects.order_by('school_class')
    return render(request, 'students/student_list.html', {'students': students})

# Ta funkcja sortuje listę studentów po odległości do szkoły.
def sort_by_distance(request):
    students = Student.objects.order_by('distance_to_school')
    return render(request, 'students/student_list.html', {'students': students})

# Ta funkcja obsługuje żądanie usunięcia studenta.
@csrf_exempt
def delete_student(request, student_id):
    if request.method == 'DELETE':
        try:
            student = Student.objects.get(id=student_id)
            student.delete()
            return JsonResponse({'message': 'Uczeń został pomyślnie usunięty.'})
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Uczeń o podanym ID nie istnieje.'}, status=404)
    else:
        return JsonResponse({'error': 'Nieprawidłowa metoda żądania.'}, status=400)
