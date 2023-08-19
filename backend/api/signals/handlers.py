from api.models import Corporation,EsgScore
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.conf import settings
from api.tasks import scrape_corp,scrape_esg

@receiver(post_save, sender=Corporation)
def scrape_corporation(sender, **kwargs):
    print('start the scraping')
    scrape_corp.delay()
