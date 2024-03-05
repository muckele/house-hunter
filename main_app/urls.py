from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('homes/', views.home_index, name='home-index'),
  path('homes/<int:home_id>', views.home_detail, name='home-detail'),

]