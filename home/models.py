from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=1)
    domain = models.CharField(max_length=30)
    resume_link = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    experience = models.IntegerField()
    education = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.name