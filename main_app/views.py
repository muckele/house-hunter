from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Home

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def home_index(request):
  homes = Home.objects.all()
  return render(request, 'homes/index.html', { 'homes': homes })

def home_detail(request, home_id):
  home = Home.objects.get(id=home_id)
  return render(request, 'homes/detail.html', { 'home': home })

class HomeCreate(CreateView):
  model = Home
  fields = '__all__'
