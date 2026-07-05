from django.shortcuts import render
from .models import DeviationLog

def deviation_dashboard(request):
    open_deviations = DeviationLog.objects.filter(status='open').count()
    context = {'open_deviations': open_deviations}
    return render(request, 'deviations/dashboard.html', context)
