from django.db import models
from django.conf import settings
import os

# Create your models here.

class EntropyCalc(models.Model):
    title = models.CharField(max_length=100, blank=True)
    csv_file = models.FileField(upload_to='input_csv/%Y/%m/%d', blank=True)
    output = models.FileField(upload_to='output_csv/%Y/%m/%d', blank=True, default=os.path.join(settings.BASE_DIR, 'media', 'output.csv'))

    def __str__(self):
        return self.title