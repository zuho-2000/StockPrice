from django.conf import settings
from django.db import models
from django.utils import timezone


class Item(models.Model):
    iName = models.CharField(max_length=20)
    genre = models.CharField(max_length=10)
    stock = models.PositiveSmallIntegerField()

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

    def __str__(self):
        return (self.price*self.volume)