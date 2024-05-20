from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .models import Corporation
from .serializers import CorporationSerializer, EsgSerializer, UserSerializer
from .filters import EsgFilter
from django.contrib.auth import get_user_model
from .permissions import IsSuperUserOrStaffReadOnly


class CorporationViewSet(ModelViewSet):
    queryset = Corporation.objects.all()
    serializer_class = CorporationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'industry_type','id']
    permissions_classes = [IsSuperUserOrStaffReadOnly]

class EsgViewSet(ModelViewSet):
    queryset = Corporation.objects.all()
    serializer_class = EsgSerializer
    lookup_field = 'ticker'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EsgFilter
    ordering_fields = ['esg_score', 'rank', 'environment_pillar', 'social_pillar', 'governance_pillar']
    permissions_classes = [IsSuperUserOrStaffReadOnly]

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permissions_classes = [IsSuperUserOrStaffReadOnly]

