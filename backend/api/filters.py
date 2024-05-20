from django_filters.rest_framework import FilterSet
from .models import Corporation


class EsgFilter(FilterSet):
    class Meta:
        model = Corporation
        fields = {
            'esg_score': ['exact', 'gt', 'lt'],
            'rank': ['exact', 'gt', 'lt'],
        }

