from django.db import models
from datetime import date
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_description = models.TextField()
    responsibilities = models.TextField(null=True)
    company_details = models.TextField(null=True)
    place = models.CharField(max_length=100,null=True)
    domain = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date = models.DateField(default=date.today,null=True)
 

    def __str__(self):
        return self.title
