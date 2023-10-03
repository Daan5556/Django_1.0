from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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

def resultsblock2(request):
    if request.method == "POST":
        form = expoblock2form(request.POST)
        if form.is_valid():
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
