from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import expo1Form
import json

def index(request):
    return render(request, "home_page.html")

def results(request):
    if request.method == "POST":
        form = expo1Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data['jessebv']
            file = open("Data.txt", "w")
            file.write(str(data))
            file.close()

        return HttpResponseRedirect("/thanks/")
    else:
        form = expo1Form()
        return render(request, "home_page.html", {"form": form})

def thanks(request):
    return render(request, "thankYou.html")
