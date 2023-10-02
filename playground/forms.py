from django import forms

class expo1Form(forms.Form):
    leerlingnummer = forms.CharField(label='leerlingnummer', max_length=10)
    jesse = forms.CharField(label='jesse', max_length=10)
    yvocomm = forms.CharField(label='yvocomm', max_length=10)
    jessebv = forms.CharField(label='jessebv', max_length=10)
