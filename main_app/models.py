from django.db import models
from django.urls import reverse

HOME_TYPES = (
  ('house', 'House'),
  ('lot', 'Lot'),
  ('multifamily', 'Multi-family'),
  ('condo', 'Condominium'),
  ('townhomes', 'Townhomes'),
)


# Create your models here.
class Home(models.Model):
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
  type = models.CharField(max_length=50, choices=HOME_TYPES, default=HOME_TYPES[0][0])
  property_taxes = models.IntegerField()
  original_url = models.URLField(max_length=255, verbose_name="Original URL", null=True)

  def __str__(self):
    return self.address
  
  def get_absolute_url(self):
    return reverse('home-detail', kwargs={'home_id': self.id})
  
