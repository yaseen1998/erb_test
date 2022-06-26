from django.urls import path

from .views import *

urlpatterns = [
 
    path("team/", TeamList.as_view()),
    path("F/", FilterFootballerView.as_view()),
    path("Q/", QFootballerView.as_view()),
    path("A/", AnnotateView.as_view()),
    path("G/", AggregationView.as_view()),

]