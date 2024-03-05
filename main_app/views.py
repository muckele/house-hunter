from django.shortcuts import render
from .models import Home

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def home_index(request):
  homes = Home.objects.all()
  return render(request, 'homes/index.html', { 'homes': homes })
