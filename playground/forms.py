from django import forms

class expo1Form(forms.Form):
    leerlingnummer = forms.CharField(label='leerlingnummer', max_length=10)
    jesse = forms.CharField(label='jesse', max_length=10)
    yvocomm = forms.CharField(label='yvocomm', max_length=10)
    jessebv = forms.CharField(label='jessebv', max_length=10)

class expoblock1form(forms.Form):
    leerlingnummer = forms.CharField(label="leerlingnummer", max_length=6)
    spinazie = forms.CharField(label="spinazie", max_length=1)
    mozzarella = forms.CharField(label="mozzarella", max_length=1)
    spareribs = forms.CharField(label="spareribs", max_length=1)
    spaghetti = forms.CharField(label="spaghetti", max_length=1)
    noodles = forms.CharField(label="noodles", max_length=1)
    salami = forms.CharField(label="salami", max_length=1)

class expoblock2form(forms.Form):
    leerlingnummer = forms.CharField(label="leerlingnummer", max_length=6)
    avocado = forms.CharField(label="avocado", max_length=1)
    kiwi = forms.CharField(label="kiwi", max_length=1)
    mango = forms.CharField(label="mango", max_length=1)
    bloemkool = forms.CharField(label="bloemkool", max_length=1)
    aardbei = forms.CharField(label="aardbei", max_length=1)