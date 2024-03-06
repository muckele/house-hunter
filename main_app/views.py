from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import House


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def house_index(request):
  houses = House.objects.all()
  return render(request, 'houses/index.html', { 'houses': houses })

@login_required
def house_detail(request, house_id):
  house = House.objects.get(id=house_id)
  return render(request, 'houses/detail.html', { 'house': house })

class HouseCreate(LoginRequiredMixin, CreateView):
  model = House
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)  


class HouseUpdate(LoginRequiredMixin, UpdateView):
  model = House
  fields = '__all__'

class HouseDelete(LoginRequiredMixin, DeleteView):
  model = House
  success_url = '/houses/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)