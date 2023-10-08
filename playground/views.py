from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from.forms import expoblock1form
from.forms import expoblock2form

def index(request):
    return render(request, "home_page.html")
def expoblock1(request):
    return render(request, "expoBlock1.html")

def expoblock2(request):
    return render(request, "expoBlock2.html")

def results(request):
    if request.method == "POST":
        form = expo1Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data['jessebv']
            file = open("Data.txt", "a")
            file.write(str("\n") + str(data))
            file.close()

        return HttpResponseRedirect("/thanks/")
    else:
        form = expo1Form()
        return render(request, "home_page.html", {"form": form})

def is_leerlingnummer_duplicate1(leerlingnummer):
    # Read the existing file to check for duplicates
    with open("expoBlock1.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if leerlingnummer in line:
                return True
    return False

def resultsblock1(request):
    if request.method == "POST":
        form = expoblock1form(request.POST)
        if form.is_valid():
            leerlingnummer = form.cleaned_data["leerlingnummer"]
            if is_leerlingnummer_duplicate1(leerlingnummer):
                return render(request, 'submission_error.html', {'message': 'You have already submitted the form.'})
            entryList = ["leerlingnummer", "spinazie", "mozzarella", "spareribs", "spaghetti", "noodles", "salami"]
            for i in entryList:
                dataEntry = form.cleaned_data[i]
                file = open("expoBlock1.txt", "a")
                file.write(str("\n") + str(dataEntry))
                file.close()


            return HttpResponseRedirect("/thanks/")
        return render(request, "expoBlock1.html", {"form": form})
    else:
        form = expoblock1form()
        return render(request, "expoBlock1.html", {"form": form})

def is_leerlingnummer_duplicate2(leerlingnummer):
    # Read the existing file to check for duplicates
    with open("expoBlock2.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if leerlingnummer in line:
                return True
    return False

def resultsblock2(request):
    if request.method == "POST":
        form = expoblock2form(request.POST)
        if form.is_valid():
            leerlingnummer = form.cleaned_data["leerlingnummer"]
            if is_leerlingnummer_duplicate2(leerlingnummer):
                return render(request, 'submission_error.html', {'message': 'You have already submitted the form.'})
            entryList = ["leerlingnummer", "avocado", "kiwi", "mango", "bloemkool", "aardbei"]
            for i in entryList:
                dataEntry = form.cleaned_data[i]
                file = open("expoBlock2.txt", "a")
                file.write(str("\n") + str(dataEntry))
                file.close()


            return HttpResponseRedirect("/thanks/")
        return render(request, "expoBlock2.html", {"form": form})
    else:
        form = expoblock2form()
        return render(request, "expoBlock2.html", {"form": form})


def thanks(request):
    return render(request, "thankYou.html")
