from django.shortcuts import render

from sops.models import SopDocument
from training.models import TrainingRecord
from deviations.models import DeviationLog
from capas.models import CapaAction
from documents.models import ControlledDocument

def about(request):
    
    return render(request, 'main_app/about.html')

def overview_dashboard(request):
    context = {
        'sop_count': SopDocument.objects.count(),
        'training_count': TrainingRecord.objects.count(),
        'deviation_count': DeviationLog.objects.count(),
        'capa_count': CapaAction.objects.count(),
        'document_count': ControlledDocument.objects.count(),
    }
    return render(request, 'main_app/dashboard.html', context)
