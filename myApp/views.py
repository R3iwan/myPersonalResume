from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'html/index.html')

def exp(request):
    return render(request, 'html/exp.html')

def skills(request):
    return render(request, 'html/skills.html')


