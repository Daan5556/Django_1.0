from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("thanks/", views.thanks, name="thanks"),
    path("resultsblock1/", views.resultsblock1, name="results1"),
    path("resultsblock2/", views.resultsblock2, name="results2"),
    path("expoblock1/", views.expoblock1, name="expoblock1"),
    path("expoblock2/", views.expoblock2, name="expoblock2"),


]