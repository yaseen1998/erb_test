from django.shortcuts import render, redirect
from dynamic_models.models import ModelSchema, FieldSchema
from django.urls import clear_url_caches
from importlib import import_module,reload
from django.contrib import admin
from django.conf import settings
from .models import Modelnames
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def addModelEntries(request):
#     res = {'success' : False}
#     return Response(res)

# def base(request):
#     res = {'success' : False}
#     return Response(res)


class CreateModels(APIView):
    def post(self,request):
        data = request.data
        modelExists = False
        modelCreated = False
        try :
            model_schema = ModelSchema.objects.create(name=data['modelname'])
            modelCreated = True
        except Exception as e:
            modelExists = True
            return Response({'success' : False, 'message' : 'Model already exists'})
        # for x in range(len_req):
        field_schema = FieldSchema.objects.create(
            name=data['field'],
            data_type=data['datatype'],
            model_schema=model_schema,
            max_length=100,
            null=True,
            unique=False
            )
        model_create = Modelnames.objects.create(modelname=data['modelname'])
        reg_model = model_schema.as_model()
        admin.site.register(reg_model)
        reload(import_module(settings.ROOT_URLCONF))
        clear_url_caches()
        return Response({'success' : True, 'message' : 'Model created successfully'})

# def showObjectLists(request):
#     modelNamesQuerySet = Modelnames.objects.all()
#     modelNames = list()
#     for model in modelNamesQuerySet:
#         modelNames.append(model.modelname)
#     cont_dict = {
#         'modelNames' : modelNames,
#         'get' : True
#     }
#     if data:
#         model = ModelSchema.objects.get(name=data['modelname']).as_model()
#         objList = model.objects.all().values()
#         fieldNames = list()
#         noEntry = False
#         try:
#             for x in objList[0]:
#                 fieldNames.append(x)
#         except Exception as e:
#             noEntry = True
#         cont_dict = {
#             'modelNames' : modelNames,
#             'objects' : objList,
#             'noEntry' : noEntry,
#             'fieldNames' : fieldNames,
#             'objectType' : data['modelname'],
#             'get' : False
#         }
#     return render(request, 'displayObjects.html', context = cont_dict)