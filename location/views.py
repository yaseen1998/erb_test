from django.shortcuts import render
from . import utilities
from rest_framework.views import APIView
from rest_framework.response import Response
import json

class LocationView(APIView):
    
    def post(self,request):
        data= request.data
        address = data['address']
        location = utilities.location_by_address(address)
        context = {
            'latitude':location['lat'],
            'longitude':location['lon']
        }
        return Response(context)
        
class ViewLocation(APIView):
    
    def post(self,request):
        data= request.data
        lat = data['lat']
        lon = data['lon']
        address = utilities.address_by_location(lat,lon)
        context = {
            'address':str(address)
        }
        print(address)
        return Response(context)
        
