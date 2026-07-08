from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SopDocument
from .forms import SopDocumentForm

@login_required
def sop_dashboard(request):
    sops_list = SopDocument.objects.all().order_by('-created_at')
    context = {
        'sops': sops_list, 
        'sop_count': sops_list.count()
        }
    return render(request, 'sops/dashboard.html', context)

def sop_create(request):
    if request.method == 'POST':
        form = SopDocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sops:dashboard')
    else:
        form = SopDocumentForm()
            
    return render(request, 'sops/sop_form.html', {'form': form})
    
def sop_update(request, pk):
    sop = get_object_or_404(SopDocument, pk=pk)
    if request.method == 'POST':
        form = SopDocumentForm(request.POST, instance=sop)
        if form.is_valid():
            form.save()
            return redirect('sops:dashboard')
    else:
        form = SopDocumentForm(instance=sop)
        
    return render(request, 'sops/sop_form.html', {'form': form})

def sop_delete(request, pk):
    sop = get_object_or_404(SopDocument, pk=pk)
    if request.method == 'POST':
        sop.delete()
        return redirect('sops:dashboard')
    return render(request, 'sops/sop_confirm_delete.html', {'sop': sop})

def sop_detail(request, pk):
    sop = get_object_or_404(SopDocument, pk=pk)
    return render(request, 'sops/sop_detail.html', {'sop': sop})
        