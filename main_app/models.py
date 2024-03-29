from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

HOUSE_TYPES = (
  ('house', 'House'),
  ('lot', 'Lot'),
  ('multifamily', 'Multi-family'),
  ('condo', 'Condominium'),
  ('townhome', 'Townhome'),
)


# Create your models here.
class House(models.Model):
  price = models.IntegerField()
  address = models.CharField(max_length=255)
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
  sqft = models.IntegerField()
  description = models.TextField()
  lotsize = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Lot Size")
  tax_assessment = models.IntegerField()
  tax_year = models.IntegerField()
  listed_by = models.CharField(max_length=255)
  type = models.CharField(max_length=50, choices=HOUSE_TYPES, default=HOUSE_TYPES[0][0])
  property_taxes = models.IntegerField()
  original_url = models.URLField(max_length=255, verbose_name="Original URL", null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.address
  
  def get_absolute_url(self):
    return reverse('house-detail', kwargs={'house_id': self.id})
  
class Photo(models.Model):
  url = models.CharField(max_length=250)
  house = models.OneToOneField(House, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for house_id: {self.house_id} @{self.url}"
  
