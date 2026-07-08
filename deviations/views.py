from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DeviationLog
from .forms import DeviationLogForm

@login_required
def deviation_dashboard(request):
    deviations = DeviationLog.objects.all().order_by('-created_at')
    return render(request, 'deviations/dashboard.html', {'deviations': deviations, 'deviation_count': deviations.count()})

def deviation_create(request):
    if request.method == 'POST':
        form = DeviationLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deviations:dashboard')
    else:
        form = DeviationLogForm()
    return render(request, 'deviations/deviation_form.html', {'form': form})

def deviation_detail(request, pk):
    deviation = get_object_or_404(DeviationLog, pk=pk)
    return render(request, 'deviations/deviation_detail.html', {'deviation': deviation})

def deviation_update(request, pk):
    deviation = get_object_or_404(DeviationLog, pk=pk)
    if request.method == 'POST':
        form = DeviationLogForm(request.POST, instance=deviation)
        if form.is_valid():
            form.save()
            return redirect('deviations:dashboard')
    else:
        form = DeviationLogForm(instance=deviation)
    return render(request, 'deviations/deviation_form.html', {'form': form})

def deviation_delete(request, pk):
    deviation = get_object_or_404(DeviationLog, pk=pk)
    if request.method == 'POST':
        deviation.delete()
        return redirect('deviations:dashboard')
    return render(request, 'deviations/deviation_confirm_delete.html', {'deviation': deviation})