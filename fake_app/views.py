from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User
from fake_app.models import Model
class AddData(APIView):
    def get(self, request):
        model = Model.objects.using('user').create(name='Model1')
        return Response({'status': 'ok'})