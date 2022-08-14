from django.db import models
from django.contrib.auth.models import User

class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    coingecko_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CoinPrice(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.price

class PriceAlert(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.price