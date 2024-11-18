from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    photo = models.ImageField(upload_to='newevents/', null=True, blank=True)

    def __str__(self):
        return self.titre

class Card(models.Model):
    event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='card/', null=True, blank=True)

    def __str__(self):
        return self.title

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    path = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.ip_address} visited {self.path} on {self.timestamp}"

class PlayedTrack(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    played_at = models.DateTimeField(auto_now_add=True)

class Sale(models.Model):
    date = models.DateField()
    amount = models.FloatField()

class Animateur(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class emissions(models.Model):
    titre = models.CharField(max_length=100)
    animateur = models.CharField(max_length=100)
    jour = models.CharField(max_length=10, blank=True, null=True)
    horaires = models.CharField(max_length=20, blank=True, null=True)
    frequances = models.CharField(max_length=100, blank=True, null=True)
    lien = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.titre

class Stats(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    date = models.DateField()
    ip = models.CharField(max_length=100)

# .py

class Show(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=9, choices=[
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendedi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    ])
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.day_of_week} ({self.start_time} - {self.end_time})"
