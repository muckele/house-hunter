from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('houses/', views.house_index, name='house-index'),
  path('houses/<int:house_id>', views.house_detail, name='house-detail'),
  path('houses/create/', views.HouseCreate.as_view(), name='house-create'),
  path('houses/<int:pk>/update/', views.HouseUpdate.as_view(), name='house-update'),
  path('houses/<int:pk>/delete/', views.HouseDelete.as_view(), name='house-delete'),
  path('accounts/signup/', views.signup, name='signup'),

]