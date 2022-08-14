from django.urls import path
from core.views import Prices
urlpatterns = [
    path('prices/btc',Prices.as_view(),name='prices'),
]