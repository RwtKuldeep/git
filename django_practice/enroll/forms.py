from django import forms
from .models import Student


class Student_info(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_no']
