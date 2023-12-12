from django.shortcuts import render
from .models import Student
from .forms import Student_info
# Create your views here.


def home(request):
    if request.method == "POST":
        fm = Student_info(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Student_info()
    return render(request, 'enroll/index.html', {'form': fm})
