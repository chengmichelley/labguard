from django.shortcuts import render, redirect, get_object_or_404
from .models import CapaAction
from .forms import CapaActionForm

def capa_dashboard(request):
    capas = CapaAction.objects.all().order_by('-due_date')
    return render(request, 'capas/dashboard.html', {'capas': capas, 'capa_count': capas.count()})

def capa_create(request):
    if request.method == 'POST':
        form = CapaActionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capas:dashboard')
    else:
        form = CapaActionForm()
    return render(request, 'capas/capa_form.html', {'form': form})

def capa_detail(request, pk):
    capa = get_object_or_404(CapaAction, pk=pk)
    return render(request, 'capas/capa_detail.html', {'capa': capa})

def capa_update(request, pk):
    capa = get_object_or_404(CapaAction, pk=pk)
    if request.method == 'POST':
        form = CapaActionForm(request.POST, instance=capa)
        if form.is_valid():
            form.save()
            return redirect('capas:dashboard')
    else:
        form = CapaActionForm(instance=capa)
    return render(request, 'capas/capa_form.html', {'form': form})

def capa_delete(request, pk):
    capa = get_object_or_404(CapaAction, pk=pk)
    if request.method == 'POST':
        capa.delete()
        return redirect('capas:dashboard')
    return render(request, 'capas/capa_confirm_delete.html', {'capa': capa})