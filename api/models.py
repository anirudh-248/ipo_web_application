from django.db import models

# Create your models here.
class IpoInfo(models.Model):
    company_logo_path = models.TextField(max_length=500)
    company_name = models.CharField(max_length=100)
    price_band = models.CharField(max_length=100)
    open_date = models.CharField(max_length=100)
    close_date = models.CharField(max_length=100)
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    ipo_price = models.CharField(max_length=100)
    listing_price = models.CharField(max_length=100)
    listing_gain = models.CharField(max_length=100)
    listing_date = models.CharField(max_length=100)
    cmp = models.CharField(max_length=100)
    current_return = models.CharField(max_length=100)
    rhp = models.CharField(max_length=100)
    drhp = models.CharField(max_length=100)