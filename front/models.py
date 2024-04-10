from django.db import models

# Create your models here.
class Appointment(models.Model):
    title = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )

    doctor = models.CharField(
        max_length = 255,
        null = True,
        blank = False,
    )

    start = models.DateTimeField(
        null = False,
        blank = False
    )

    end = models.DateTimeField(
        null = False,
        blank = False
    )

class Patient(models.Model):
    name = models.CharField(max_length = 255, blank = False)
    birth_date = models.DateField(null = True, blank = False)

class Doctor(models.Model):
    name = models.CharField(max_length = 255, blank = False)
    specialty = models.CharField(max_length = 100, null = True, blank = False)
    birth_date = models.DateField(null = True, blank = False)

class Product(models.Model):
    name = models.CharField(max_length = 255, blank = False)

    CHOICES = (
        ("Farmaco", "Farmaco"),
        ("Instrumento", "Instrumento")
    )
    product_type = models.CharField(max_length=11, choices=CHOICES, null = True, blank = True)

    expiration = models.DateField(null = True, blank = False)