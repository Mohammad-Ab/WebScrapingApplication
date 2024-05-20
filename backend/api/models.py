from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from django.contrib import admin

# Create your models here.

class Corporation(models.Model):
    title = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255, unique=True)
    industry_type = models.TextField(blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class EsgScore(models.Model):
    rank = models.IntegerField()
    total_industries = models.IntegerField(validators=[MinValueValidator(0)])
    esg_score = models.IntegerField()
    environment_pillar = models.IntegerField()
    social_pillar = models.IntegerField()
    governance_pillar = models.IntegerField()
    corporation = models.OneToOneField(Corporation, on_delete=models.CASCADE, primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return self.corporation
    
    class Meta:
        ordering = ['esg_score','rank']
        '''permissions = [
                    ('rest_scores', 'can reset all score')
                ]
        '''


