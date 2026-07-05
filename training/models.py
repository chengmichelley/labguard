from django.db import models

class TrainingRecord(models.Model):
    employee_name = models.CharField(max_length = 255)
    status = models.CharField(max_length = 50, default = 'overdue')
