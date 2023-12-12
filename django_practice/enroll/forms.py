from django import forms
from .models import Student


class Student_info(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_no']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Your Name', 'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'placeholder': 'Enter Your Name', 'class': 'form-control'})
        }
