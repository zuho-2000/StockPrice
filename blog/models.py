from unicodedata import name
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Item(models.Model):
    iName = models.CharField(max_length=20)
    genre = models.CharField(max_length=10)
    stock = models.PositiveSmallIntegerField(default=0)
    under = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.iName


class Shop(models.Model):
    sName = models.CharField(max_length=20)
    area = models.CharField(max_length=20)

    def __str__(self):
        return self.sName


class Price(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    day = models.DateTimeField(default=timezone.now)
    price = models.PositiveIntegerField()
    volume = models.PositiveSmallIntegerField()
    unit_price=models.FloatField(default=0)

    @property
    def price_Calculation(self, *args, **kwargs):
        return round(self.price / self.volume ,2)

    def save(self, *args, **kwargs):
        self.unit_price = self.price_Calculation
        super(Price, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.item) + " " + str(self.shop)