from django.db import models

class SopDocument(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('under_review', 'Under Review'),
        ('effective', 'Effective'),
        ('archived', 'Archived')
    ]
    title = models.CharField(max_length = 255)
    doc_number = models.CharField(max_length=50, unique=True)
    version = models.IntegerField(default=1)
    status = models.CharField(max_length = 50, default= 'pending_review')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.doc_number}: {self.title} (v{self.version})'
