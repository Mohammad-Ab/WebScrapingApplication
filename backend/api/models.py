from django.db import models
from django.contrib import admin

class Corporation(models.Model):
    title = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255, unique=True)
    industry_type = models.TextField(blank=True)
    rank = models.IntegerField()
    total_industries = models.IntegerField()
    esg_score = models.IntegerField()
    environment_pillar = models.IntegerField()
    social_pillar = models.IntegerField()
    governance_pillar = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title','esg_score','rank']


