from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Special=models.CharField(max_length=50)

class Patient(models.Model):
    Gender_choice=(
        ('M', 'Male'),
        ('F', 'Female')
        ('O', 'Other')
    )
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=1,choices=Gender_choice)
    Age=models.PositiveIntegerField()
    Address=models.CharField(max_length=100)

class Appoinment(models.Model):
    Doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()


