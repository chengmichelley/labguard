from django.db import models

class ControlledDocuments(models.Model):
    filename = models.CharField(max_length= 255)
    version = models.IntegerField(default= 1)
