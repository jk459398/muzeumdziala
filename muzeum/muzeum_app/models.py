from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError
from django import forms

class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)

    def clean(self):
        if self.birth_year and self.death_year and self.death_year < self.birth_year:
            raise ValidationError({'death_year': 'Rok śmierci nie może być wcześniejszy niż rok urodzenia.'})

    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.birth_year} - {self.death_year if self.death_year else 'obecnie'})"
    
class Size(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.FloatField()
    width = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return f"Height: {self.height}, Width: {self.width}, Weight: {self.weight}"
    
class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Institution(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Eksponat(models.Model):
    STATUS_CHOICES = [
        ('magazine', 'Magazyn (konserwacja)'),
        ('gallery', 'Wystawiony w galerii'),
        ('loaned', 'Wypożyczony'),
        ('available', 'Dostępny do wypożyczenia'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)    
    type = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    cenny = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.type} - {self.artist}"


class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    exhibit = models.ForeignKey(Eksponat, on_delete=models.CASCADE)
    place = models.ForeignKey(Institution, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.exhibit.title} - {self.institution_name}"
    

class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    exhibit = models.ForeignKey(Eksponat, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

