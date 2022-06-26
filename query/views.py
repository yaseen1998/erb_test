from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import F,Q,Sum

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
class CompetioinList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    
class FooTballerList(generics.ListCreateAPIView):
    queryset = FooTballer.objects.all()
    serializer_class = FooTballerSerializer
    
class FilterFootballerView(APIView):
    def get(self, request, *args, **kwargs):

        footballers = FooTballer.objects.filter( seasson_assists__gt=F('season_goals')) # get all footballers with more assists than goals
        serializer = FooTballerSerializer(footballers, many=True)
        return Response(serializer.data)
    

class QFootballerView(APIView):
    def get(self, request, *args, **kwargs):
        footballers = FooTballer.objects.filter(~Q(age__lt=16) | Q(season_goals__gt=10)) # ~Q(age__lt=16) is not age__lt=16
        serializer = FooTballerSerializer(footballers, many=True)
        return Response(serializer.data)
    
class AnnotateView(APIView):
    def get(self,request):
        footballer = FooTballer.objects.annotate(age_goal = F('age') + F('season_goals'))
        resutl = []
        for football in footballer :
            resutl.append([football.name,football.age_goal])
        return Response(resutl)
    
class AggregationView(APIView):
    def get(self,request):
        foot = FooTballer.objects.all().aggregate(total_season_goals = Sum('season_goals'))
        return Response(foot)
    