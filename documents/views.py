from django.shortcuts import render, redirect, get_object_or_404
from .models import ControlledDocument
from .forms import ControlledDocumentForm

def document_dashboard(request):
    docs = ControlledDocument.objects.all().order_by('-uploaded_at')
    return render(request, 'documents/dashboard.html', {'docs': docs, 'doc_count': docs.count()})

def document_create(request):
    if request.method == 'POST':
        form = ControlledDocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('documents:dashboard')
    else:
        form = ControlledDocumentForm()
    return render(request, 'documents/document_form.html', {'form': form})

def document_detail(request, pk):
    doc = get_object_or_404(ControlledDocument, pk=pk)
    return render(request, 'documents/document_detail.html', {'doc': doc})

def document_update(request, pk):
    doc = get_object_or_404(ControlledDocument, pk=pk)
    if request.method == 'POST':
        form = ControlledDocumentForm(request.POST, instance=doc)
        if form.is_valid():
            form.save()
            return redirect('documents:dashboard')
    else:
        form = ControlledDocumentForm(instance=doc)
    return render(request, 'documents/document_form.html', {'form': form})

def document_delete(request, pk):
    doc = get_object_or_404(ControlledDocument, pk=pk)
    if request.method == 'POST':
        doc.delete()
        return redirect('documents:dashboard')
    return render(request, 'documents/document_confirm_delete.html', {'doc': doc})