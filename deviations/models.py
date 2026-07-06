from django.db import models

class DeviationLog(models.Model):
    STATUS_CHOICES = [
        ('investigation', 'Under Investigation'),
        ('pending_qa', 'Pending QA Review'),
        ('resolved', 'Resolved')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    immediate_action_taken = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='investigation')
    discovered_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    related_sop = models.ForeignKey('sops.SopDocument', on_delete= models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'DEV-{self.id}: {self.title}'
    