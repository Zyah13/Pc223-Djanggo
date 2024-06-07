from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id_number', 'lastname', 'firstname', 'middle_initial', 'gender', 'birthdate', 'email_address', 'year_level', 'course', 'image']
        labels = {
            'id_number': 'ID Number',
            'lastname': 'Last Name',
            'firstname': 'First Name',
            'middle_initial': 'Middle Initial',
            'gender': 'Gender',
            'birthdate': 'Birthdate',
            'email_address': 'Email Address',
            'year_level': 'Year Level',
            'course': 'Course',
            'image': 'Upload Image'
        }
        widgets = {
            'id_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_initial': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'year_level': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }