from django.db import models

class DeviationLog(models.Model):
    description = models.TextField()
    status = models.CharField(max_length=50, default='open')