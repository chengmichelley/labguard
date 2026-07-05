from django.shortcuts import render
from .models import TrainingRecord

def training_dashboard(request):
    overdue_count = TrainingRecord.objects.filter(status='overdue').count()
    context = {'overdue_count': overdue_count}
    return render(request, 'training/dashboard.html', context)