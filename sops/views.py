from django.shortcuts import render
from .models import SopDocument

def sop_dashboard(request):
    total_sops = SopDocument.objects.count()
    context = {'total_sops': total_sops}
    return render(request, 'sops/dashboard.html', context)