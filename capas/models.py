from django.db import models

class CapaAction(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('effectiveness_check', 'Under Effectiveness Review'),
        ('closed', 'Closed'),
    ]
    title = models.CharField(max_length= 255)
    root_cause = models.TextField(null=True, blank=True)
    preventive_action = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default='open')
    due_date = models.DateField(null=True, blank=True)
    is_effective = models.BooleanField(null=True, blank=True)
    
    related_deviation = models.OneToOneField('deviations.DeviationLog', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'CAPA-{self.id}: {self.title}'
    