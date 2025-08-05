# backend/site1/views.py (or new views file)
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')
