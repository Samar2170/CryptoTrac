from rest_framework.serializers import ModelSerializer
from core.models import CoinPrice, Coin 

class CoinSz(ModelSerializer):
    class Meta:
        model = Coin
        fields = ['name','symbol']

class CoinPriceSz(ModelSerializer):
    coin = CoinSz()
    class Meta:
        model = CoinPrice
        fields = ['coin', 'price', 'timestamp']