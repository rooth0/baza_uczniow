from django import forms
from .models import Student

# Formularz do tworzenia i edycji obiektów modelu Student.
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'address', 'distance_to_school', 'school_class']
