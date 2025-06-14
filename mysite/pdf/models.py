from django.db import models

# Create your models here.
class Profile(models.Model):
    TEMPLATE_CHOICES = [
    ('template1', 'Classic'),
    ('template2', 'Modern'),
    ('template3', 'Elegant'),]

    name=models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    experience = models.TextField(max_length=1000)
    skills= models.TextField(max_length=1000)
    template_choice = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, default='template1')