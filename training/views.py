from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TrainingRecord
from .forms import TrainingRecordForm

@login_required
def training_dashboard(request):
    records = TrainingRecord.objects.all().order_by('-due_date')
    return render(request, 'training/dashboard.html', {'records': records, 'record_count': records.count()})

def training_create(request):
    if request.method == 'POST':
        form = TrainingRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training:dashboard')
    else:
        form = TrainingRecordForm()
    return render(request, 'training/training_form.html', {'form': form})

def training_detail(request, pk):
    record = get_object_or_404(TrainingRecord, pk=pk)
    return render(request, 'training/training_detail.html', {'record': record})

def training_update(request, pk):
    record = get_object_or_404(TrainingRecord, pk=pk)
    if request.method == 'POST':
        form = TrainingRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('training:dashboard')
    else:
        form = TrainingRecordForm(instance=record)
    return render(request, 'training/training_form.html', {'form': form})

def training_delete(request, pk):
    record = get_object_or_404(TrainingRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('training:dashboard')
    return render(request, 'training/training_confirm_delete.html', {'record': record})