 
from rest_framework import serializers
from .models import Agedistribution, Monthlydistribution ,Policestdistribution, Yearlydistribution, unidentifieddeadbodies

class AgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agedistribution
        fields = '__all__'

class MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monthlydistribution
        fields = '__all__'

class PoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policestdistribution
        fields = '__all__'

class YearwiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yearlydistribution
        fields = '__all__'

class UnidentifiedBodies(serializers.ModelSerializer):
    class Meta:
        model = unidentifieddeadbodies
        fields = '__all__' 


