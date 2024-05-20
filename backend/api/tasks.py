#for tasks
from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery import app, shared_task

from .models import Corporation,EsgScore

#for scraping
import requests
import json

#for logging
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

#Scraping Function For Corporation
@shared_task()
def scrape_corp():
    req = requests.get('https://www.refinitiv.com/bin/esg/esgsearchsuggestions')
    data = req.json()
    for k in data:
        try:
            Corporation.objects.create(
                        title = k['companyName'],
                        ticker = k['ricCode'],
                    )
        except Exception as e:
            print('Failed at get Json Data')
            print(e) 

    return print("Compelete level one")


@shared_task()
def scrape_esg():
    data_count = Corporation.objects.values_list('ticker', flat=True).distinct()
    print(data_count)
    for code in data_count:
        print(code)
        req = requests.get(f"https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode={code}")
        data = req.json()
        check_dict={}
        print(data)
        for k in data:
            if k == 'industryComparison':
                check_dict['industryType'] = data['industryComparison']['industryType']
                check_dict['rank'] = data['industryComparison']['rank']
                check_dict['totalIndustries'] = data['industryComparison']['totalIndustries']
            else:
                check_dict['EnvironmentPillar'] = data['esgScore']['TR.EnvironmentPillar']['score']
                check_dict['SocialPillar'] = data['esgScore']['TR.SocialPillar']['score']
                check_dict['GovernancePillar'] = data['esgScore']['TR.GovernancePillar']['score']
                check_dict['Esg'] = data['esgScore']['TR.TRESG']['score']
        print(check_dict)

        data_update = Corporation.objects.get(ticker=code)
        data_update.industry_type = check_dict['industryType']
        data_update.save(['industry_type'])

        EsgScore.objects.create(
                    rank = check_dict['rank'],
                    total_industries = check_dict['totalIndustries'],
                    environment_pillar = check_dict['EnvironmentPillar'],
                    social_pillar = check_dict['SocialPillar'],
                    governance_pillar = check_dict['GovernancePillar'],
                    esg_score = check_dict['Esg'],
                )
    return print("Compelete level Two")

def main():
    scrape_corp()
    scrape_esg()

main()




