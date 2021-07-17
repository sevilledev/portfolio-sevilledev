from django.shortcuts import render
from .models import *

# Create your views here.

def resume(request):
    edu_exps = Experience.objects.filter(category__name="Education Experience")
    work_exps = Experience.objects.filter(category__name="Work Experience")
    context = {
        'edu_exps': edu_exps,
        'work_exps': work_exps
    }
    return render(request, 'resume.html', context)