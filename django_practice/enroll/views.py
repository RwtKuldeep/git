from django.shortcuts import render
from .models import Student
from .forms import Student_info
# Create your views here.


def home(request):
    fm = Student_info()
    return render(request, 'enroll/index.html', {'form': fm})
