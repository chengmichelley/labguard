from django.db import models

class ControlledDocument(models.Model):
    title = models.CharField(max_length=255)
    filename = models.CharField(max_length= 255)
    category = models.CharField(max_length=100, default='General Documentation')
    document_url = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
