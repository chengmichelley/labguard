from django.shortcuts import render
from .models import ControlledDocuments

def document_dashboard(request):
    total_docs = ControlledDocuments.objects.count()
    context = {'total_docs': total_docs}
    return render(request, 'documents/dashboard.html', context)