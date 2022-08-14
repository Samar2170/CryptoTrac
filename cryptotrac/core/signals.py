from django.db.models.signals import post_save
from django.dispatch import receiver
from core.tasks import send_price_alert_mail

@receiver(post_save, sender='core.CoinPrice')
def coin_price_post_save(sender, instance, created, **kwargs):
    if created:
        send_price_alert_mail.delay(instance.price)

