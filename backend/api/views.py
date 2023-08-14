from django.shortcuts import render
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Corporation, EsgScore
from .serializers import CorporationSerializer, EsgScoreSerializer
from .filters import EsgScoreFilter


class CorporationViewSet(ModelViewSet):
    queryset = Corporation.objects.select_related('esgscore').all()
    serializer_class = CorporationSerializer
    filter_backends = [SearchFilter]
    #permission_classes = [ISAdminOrReadOnly]
    search_fields = ['title', 'industry_type']

    def get_serializer_context(self):
        return {'request': self.request}


class EsgScoreViewSet(ModelViewSet):
    queryset = EsgScore.objects.annotate(ticker=F('corporation__ticker'))
    serializer_class = EsgScoreSerializer
    lookup_field = 'ticker'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EsgScoreFilter
    #permission_classes = [ISAdminOrReadOnly]
    ordering_fields = ['esg_score', 'rank', 'environment_pillar', 'governance_pillar', 'social_pillar']

