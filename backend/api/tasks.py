#for tasks
from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery import app, shared_task

from .models import Corporation

#for scraping
import requests
import json
import time

#for logging
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

#Scraping Function
@shared_task()
def scrapes():
    cpreq = requests.get('https://www.refinitiv.com/bin/esg/esgsearchsuggestions')
    cp_data = cpreq.json()
    counter = 0
    try:
        for k in cp_data:
            counter+=1
            cp_ticker = k['ricCode']
            time.sleep(0.1)
            esgreq = requests.get(f"https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode={cp_ticker}", timeout=50)
            esg_data = esgreq.json()
            check_dict={}
            for e in esg_data:
                if e == 'industryComparison': 
                    check_dict['industryType'] = esg_data['industryComparison']['industryType']
                    check_dict['rank'] = esg_data['industryComparison']['rank']
                    check_dict['totalIndustries'] = esg_data['industryComparison']['totalIndustries']
                else:
                    check_dict['EnvironmentPillar'] = esg_data['esgScore']['TR.EnvironmentPillar']['score']
                    check_dict['SocialPillar'] = esg_data['esgScore']['TR.SocialPillar']['score']
                    check_dict['GovernancePillar'] = esg_data['esgScore']['TR.GovernancePillar']['score']
                    check_dict['Esg'] = esg_data['esgScore']['TR.TRESG']['score']
            print(check_dict)
            if check_dict['rank'] != "":
                Corporation.objects.create(
                        title = k['companyName'],
                        ticker = k['ricCode'],
                        industry_type = check_dict['industryType'],
                        rank = check_dict['rank'],
                        total_industries = check_dict['totalIndustries'],
                        environment_pillar = check_dict['EnvironmentPillar'],
                        social_pillar = check_dict['SocialPillar'],
                        governance_pillar = check_dict['GovernancePillar'],
                        esg_score = check_dict['Esg'],
                    )
            if counter == 200:
                return print("Done!")
        return print("Done!")
    except Exception as e:
        print("does not work!")
        print(e)

def main():

    scrapes()

main()




