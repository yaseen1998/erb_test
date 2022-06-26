from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# import pyrebase
# # Create your views here.


# firebaseConfig = {
#   "apiKey": "AIzaSyABMw32NsCZ9VUZuMf03pEEyIDFLZEZVFQ",
#   "authDomain": "flawless-agency-326910.firebaseapp.com",
#   "projectId": "flawless-agency-326910",
#   "storageBucket": "flawless-agency-326910.appspot.com",
#   "messagingSenderId": "747448779866",
#   "appId": "1:747448779866:web:c582cf87bd22f59be24463",
#   "measurementId": "G-9HL00DJLXE",
#   "databaseURL": "https://aiserviceerp-default-rtdb.firebaseio.com",
# }

# firebase=pyrebase.initialize_app(firebaseConfig)
# authe = firebase.auth()
# database=firebase.database()
# storage= firebase.storage()

# class Firebase(APIView):
      
    # def get(self, request):
    #     day = database.child('Data').child('Day').get().val()
    #     id = database.child('Data').child('Id').get().val()
    #     projectname = database.child('Data').child('Projectname').get().val()
    #     res = {'day': day, 'id': id, 'projectname': projectname}
    #     return Response(res)

    # def post(self, request):
    #     data = request.data
    #     email = data['email']
    #     password = data['password']
    #     # authe.sign_in_with_email_and_password(email, password)
    #     authe.create_user_with_email_and_password(email, password)
    #     res = {'message': 'success'}
    #     return Response(res)
    
    # def post(self, request):
    #     data = request.data
    #     file = data['file']
    #     cloud = data['cloud']
    #     storage.child(cloud).put(file)
    #     url = storage.child(cloud).get_url(file)
    #     res = {'message': url}
    #     return Response(res)
    
    
    # def post(self, request):
    #     data = request.data
    #     cloud = data['cloud']
    #     storage.child(cloud).download('test1.txt')
    #     res = {'message': 'success'}
    #     return Response(res)


# from google.colab import drive

from .models import *
from django.db import models
from fake_app.test import *
from fake_app.models import *




class Firebase(APIView):
    def get(self, request):
        model = apps.get_model('fake_app', 'model')
        print(model)
        return Response({'message': 'success'})
    def put(self, request):
        model = Model.objects.get(app__name='core', name='Person')
            # Company.add_to_class(
            # 'title',
            # models.CharField(max_length=255, blank=True, default=''),
            # )
        res = {'message': 'success'}
        return Response(res)
        
    def post(self, request):
        # model = self.create_model('Model', app_label='my_placeholder')
        
        data = request.data
        modelname = data['modelname']
        model_schema = Model.objects.create(name=modelname)
        # field = {
        #     data['name1']: getattr(models, data['type1']),
        #     # data['name2']: getattr(models, data['type2']),
        # }
        field = {
            'title1' : models.IntegerField(),
        }
        
        options = {
         'ordering': ['title1',],
        # 'verbose_name': 'valued customer',
        }
        admin_opts = {}
        model = create_models(modelname, field,
            options=options,
            admin_opts=admin_opts,
            app_label='fake_app',
            module='fake_app.models',
            )
 
        # data = request.data
        # attrs = {
        # 'name': models.CharField(max_length=32),
        # '__module__': 'account.models'
        # }
        # Animal = type("animal", (models.Model,), attrs)
        res = {'message': 'success'}
        # admin.site.register(Animal)
        # reload(import_module(settings.ROOT_URLCONF))
        # clear_url_caches()
        return Response(res)
        
 


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
SQL_URL = "sqlite:///./db.sqlite3"
engine = create_engine(
    SQL_URL, connect_args={"check_same_thread": False}
)


meta = MetaData()
# class Firebase(APIView):
    
#     def post(self, request):
#         studen = Table(
#         'fake_app_stu', meta, 
#         Column('id', Integer, primary_key = True), 
#         Column('name', String), 
#         Column('lastname', String), 
#         Column('age', Integer),
#         )
#         meta.create_all(engine)
#         attrs = {
#         'name': models.CharField(max_length=32),
#         'lastname': models.CharField(max_length=32),
#         'age': models.IntegerField(),
#         '__module__': 'fake_app.models'
#         }
#         Animal = type("stu", (models.Model,), attrs)
#         admin.site.register(Animal)
#         reload(import_module(settings.ROOT_URLCONF))
#         clear_url_caches()
#         res = {'message': 'success'}
#         return Response(res)

from django.views.decorators.cache import cache_page
from django.core.cache import cache
class CacheTest(APIView):
    def get(self, request):
        if  cache.get('test'):
            return Response({'message': 'success'})
        else :
            cache.set('test', 'test', timeout=6400)
            res = {'message': 'faild'}
            return Response(res)

        
        
