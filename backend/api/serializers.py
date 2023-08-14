from rest_framework import serializers
from .models import Corporation,EsgScore

class EsgScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = EsgScore
        exclude =['total_industries']

    corporation = serializers.StringRelatedField()
    rank = serializers.SerializerMethodField(method_name='rank_out_of')

    def rank_out_of(self,esgscore:EsgScore):
        return f'{esgscore.rank}/{esgscore.total_corporations}'

class CorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        fields = ['id','title','ticker','industry_type','esgscore']

    esgscore = EsgScoreSerializer()


