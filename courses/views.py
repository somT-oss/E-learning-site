from django.shortcuts import render
from django.db.models import Q
from .models import Course 


def home_view(request):
    # all_courses = Course.objects.all()
    # context =  {
    #     "courses": all_courses
    # }
    return render(request, 'index.html')

def course_view(request):
    all_courses = Course.objects.all()
    context =  {
        "courses": all_courses
    }
    return render(request, 'courses.html', context)
# Create your views here.
