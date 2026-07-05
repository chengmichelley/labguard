from django.db import models

class CapaAction(models.Model):
    title = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=True)