from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta  
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    image = models.ImageField(upload_to='%m/%d')

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=255)
    length_of_sess = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    detainee = models.ForeignKey(Detainee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Report(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    date_due = models.DateField(auto_now=False, auto_now_add=False)
    text_data = models.TextField()
    detainee = models.ForeignKey(Detainee, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.CharField(choices=RANK_CHOICES, null=True, max_length=15)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.role

