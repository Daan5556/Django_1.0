from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import expo1Form


def say_hello(request):
    return HttpResponse("Hello World")
def index(request):
    return render(request, "home_page.html")

def results(request):
    if request.method == "POST":
        form = expo1Form(request.POST)
        return HttpResponseRedirect("/thanks/")
    else:
        form = expo1Form()
        return render(request, "home_page.html", {"form": form})

def thanks(request):
    return render(request, "thankYou.html")
