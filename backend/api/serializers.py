from rest_framework import serializers
from .models import Corporation
from django.contrib.auth import get_user_model

class CorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        fields = ['id','title','ticker','industry_type','esg_score']

class EsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        exclude = ['ticker', 'industry_type']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


