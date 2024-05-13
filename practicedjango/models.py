from django.db import models

# Create your models here.
from django.db import models

class DataPoint(models.Model):
    data = models.CharField(max_length=255)
    timestamp = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.data} at {self.timestamp}"