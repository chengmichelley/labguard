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
    status = models.CharField(max_length = 50, choices=STATUS_CHOICES, default= 'draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    purpose_scope = models.TextField(blank=True, null=True, verbose_name='Purpose & Scope')
    roles_responsibilities = models.TextField(blank=True, null=True, verbose_name='Roles & Responsibilities')
    tools_equipment = models.TextField(blank=True, null=True, verbose_name='Required Tools & Equipment')
    procedure_steps = models.TextField(blank=True, null=True, verbose_name='Procedure Steps')
    safety_compliance = models.TextField(blank=True, null=True, verbose_name='Safety & Compliance')
    
    author_department = models.CharField(max_length=100, blank=True, null=True, verbose_name='Author/Department')
    approved_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Approvals & Signatures')
    effective_date = models.DateField(blank=True, null=True, verbose_name='Effective Date')
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.doc_number}: {self.title} (v{self.version})'
