from django.db import models

class TrainingRecord(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]
    employee_name = models.CharField(max_length = 255)
    related_sop = models.ForeignKey('sops.SopDocument', on_delete= models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length = 50, default = 'overdue')
    due_date = models.DateField()
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.employee_namename} - {self.related_sop.doc_number}'
    
