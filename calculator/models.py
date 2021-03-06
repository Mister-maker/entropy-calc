from statistics import mode
from django.db import models
from django.conf import settings
import os

# Create your models here.

class EntropyCalc(models.Model):
    CALCULATION_CHOICES = (
        ('shannon','Shannon'),
        ('tsallis', 'Tsallis'),
    )

    calculate = models.CharField(max_length=100, choices=CALCULATION_CHOICES, default='shannon')
    title = models.CharField(max_length=100, blank=True)
    csv_file = models.FileField(upload_to='input_csv/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return self.title