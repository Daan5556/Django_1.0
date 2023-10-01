from django import forms

class expo1Form(forms.Form):
    leerlingnummer = forms.CharField(max_length=10)
    jessebv = forms.CharField(max_length=10)
    yvocomm = forms.CharField(max_length=10)
    jessebv = forms.CharField(max_length=10)