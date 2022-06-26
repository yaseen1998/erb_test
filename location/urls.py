from django.urls import path

from .views import *

urlpatterns = [

    path("get/", LocationView.as_view()),
    path("get2/", ViewLocation.as_view()),
]