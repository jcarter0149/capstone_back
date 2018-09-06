from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta  

RANK_CHOICES = (
    ('Military', 'MILITARY'),
    ('Contractor', 'Contractor')
)

class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Detainee(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    date_captured = models.DateField(auto_now=False, auto_now_add=False)
    capture_location = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Report(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    date_due = models.DateField(auto_now=False, auto_now_add=False)
    text_data = models.TextField()
    detainee = models.ForeignKey(Detainee, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Session(models.Model):
    name = models.CharField(max_length=255)
    date_captured = models.DateField(auto_now=False, auto_now_add=False)
    length_of_sess = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    detainee = models.ForeignKey(Detainee, on_delete=models.CASCADE)

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Profile(models.Model):
    rank = models.CharField(choices=RANK_CHOICES, max_length=15)
    team = models.ManyToManyField(User)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
