from django.db import models

# Create your models here.


class Comic(models.Model):
    name = models.CharField(max_length=250)
    rarity = models.CharField(max_length=100)
    price = models.IntegerField()
    priceChange = models.IntegerField()
    dropPrice = models.IntegerField()
    variantIssued = models.IntegerField()
    totalIssued = models.IntegerField()
    totalListed = models.IntegerField()
