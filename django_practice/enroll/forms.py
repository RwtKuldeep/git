from django import forms
from .models import Student


class Student_info(forms.Model):
    class Meta:
        models = Student
        fields = ['name', 'email', 'phone_no']
