from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    email = forms.EmailField()
    place = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    experience = forms.IntegerField()
    education = forms.CharField(max_length=300)
    
