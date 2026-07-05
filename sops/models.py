from django.db import models

class SopDocument(models.Model):
    title = models.CharField(max_length = 255)
    status = models.CharField(max_length = 50, default= 'pending_review')
