from email.mime import image
from unittest.util import _MAX_LENGTH
from django.db import models
import os
import datetime
# Create your models here.


def filepath(reqeusts, filename):
    filename_original = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, filename_original)
    return os.path.join('comicThumbnails/', filename)


class Comic(models.Model):
    name = models.CharField(max_length=250)
    image = models.URLField("https://i.imgur.com/ShzwUoR.png")
    rarity = models.CharField(max_length=100)
    price = models.IntegerField()
    priceChange = models.IntegerField()
    dropPrice = models.IntegerField()
    variantIssued = models.IntegerField()
    totalIssued = models.IntegerField()
    totalListed = models.IntegerField()
