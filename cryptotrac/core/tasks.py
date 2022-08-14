from cryptotrac.celery import app 
from cryptotrac.settings import COINGECKO_URL
from core.models import Coin, CoinPrice
import requests
import logging
from cryptotrac.settings import MIN_PRICE, MAX_PRICE, USER_EMAIL
from django.core.mail import send_mail

HEADERS = {
    'Accept': 'application/json',
}

logger = logging.getLogger(__name__)

@app.task
def fetch_price():
    btc = Coin.objects.get(symbol='BTC')
    response = requests.get(COINGECKO_URL + "?ids="+ btc.coingecko_id +"&vs_currencies=inr", headers=HEADERS)
    data = response.json()
    price = data[btc.coingecko_id]['inr']
    CoinPrice(coin=btc, price=price).save()
    logger.info("Price of BTC is: " + str(price))


@app.task
def send_price_alert_mail(price):
    if price > float(MAX_PRICE):
        send_mail(
            'Price Alert',
            'Price of BTC is higher than ' + MAX_PRICE,
            USER_EMAIL,
            [USER_EMAIL],
            fail_silently=False,
        )
    elif price < float(MIN_PRICE):
        send_mail(
            'Price Alert',
            'Price of BTC is lower than your threshold' + MIN_PRICE,
            USER_EMAIL,
            [USER_EMAIL],
            fail_silently=False,
        )
    else:
        pass

