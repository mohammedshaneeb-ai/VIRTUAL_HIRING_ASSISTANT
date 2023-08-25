from django import forms
from .models import Job
from datetime import date

class JobForm(forms.ModelForm):
    # ...
    DOMAIN_CHOICES = [
        ('MERN', 'MERN'),
        ('Data Science', 'Data Science'),
        ('Java', 'Java'),
        ('Machine Learning', 'Machine Learning'),
        ('Data Analytics', 'Data Analytics'),
        ('Data Engineer', 'Data Engineer'),
        ('Dev Ops', 'Dev Ops'),
        ('MEAN', 'MEAN'),
        ('Flutter', 'Flutter'),
        # Add more choices as needed
    ]
    domain = forms.ChoiceField(choices=DOMAIN_CHOICES)
    date = forms.DateField(initial=date.today)
    
    class Meta:
        model = Job
        fields = ['title', 'responsibilities', 'job_description','company_details','place', 'domain','image','date']

