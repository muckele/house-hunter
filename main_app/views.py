from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Home


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def home_index(request):
  homes = Home.objects.all()
  return render(request, 'homes/index.html', { 'homes': homes })

@login_required
def home_detail(request, home_id):
  home = Home.objects.get(id=home_id)
  return render(request, 'homes/detail.html', { 'home': home })

class HomeCreate(LoginRequiredMixin, CreateView):
  model = Home
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)  


class HomeUpdate(LoginRequiredMixin, UpdateView):
  model = Home
  fields = '__all__'

class HomeDelete(LoginRequiredMixin, DeleteView):
  model = Home
  success_url = '/homes/'

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
