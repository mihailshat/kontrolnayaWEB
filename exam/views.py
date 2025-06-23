from django.shortcuts import render
from .models import msexam

def msexam_list(request):
    exams = msexam.objects.filter(is_public=True)
    context = {
        'exams': exams,
    }
    return render(request, 'exam/msexam_point6.html', context)
