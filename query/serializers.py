from dataclasses import field
from rest_framework import serializers
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'
        
class FooTballerSerializer(serializers.ModelSerializer):
    class Meta :
        model = FooTballer
        fields = '__all__'