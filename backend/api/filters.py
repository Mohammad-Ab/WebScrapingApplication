from django_filters.rest_framework import FilterSet
from .models import Corporation, EsgScore


class EsgScoreFilter(FilterSet):
    class Meta:
        model = EsgScore
        fields = {
            'esg_score': ['exact', 'gt', 'lt'],
            'rank': ['exact', 'gt', 'lt'],
            'corporation__ticker': ['exact'],
        }

