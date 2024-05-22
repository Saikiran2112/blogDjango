from django.db import models
from datetime import datetime

class posts(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=1000000)
    data=models.DateTimeField(default=datetime.now,blank=True)
