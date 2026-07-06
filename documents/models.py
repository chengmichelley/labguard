from django.db import models

class ControlledDocuments(models.Model):
    title = models.CharField(max_length=255)
    filename = models.CharField(max_length= 100)
    document_url = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
