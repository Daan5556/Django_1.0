from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path("", views.index, name="index"),
    path("", views.index, name="thanks"),
    path("", views.index, name="results"),

]