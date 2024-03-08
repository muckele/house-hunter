from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import House, Photo
import uuid
import boto3
S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'muckele-house-hunter'


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
  fields = ['price', 'address', 'bedrooms', 'bathrooms', 'sqft', 'description', 'lotsize', 'tax_assessment', 'tax_year', 'listed_by', 'type', 'property_taxes', 'original_url']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)  


class HouseUpdate(LoginRequiredMixin, UpdateView):
  model = House
  fields = ['price', 'address', 'bedrooms', 'bathrooms', 'sqft', 'description', 'lotsize', 'tax_assessment', 'tax_year', 'listed_by', 'type', 'property_taxes', 'original_url']

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
      return redirect('house-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def add_photo(request, house_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, house_id=house_id)
      house_photo = Photo.objects.filter(house_id=house_id)
      if house_photo.first():
        house_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('house-detail', house_id=house_id)
