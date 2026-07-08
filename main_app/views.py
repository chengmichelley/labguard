from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from sops.models import SopDocument
from training.models import TrainingRecord
from deviations.models import DeviationLog
from capas.models import CapaAction
from documents.models import ControlledDocument

def about(request):
    return render(request, 'main_app/about.html')

@login_required
def overview_dashboard(request):
    context = {
        'sop_count': SopDocument.objects.count(),
        'training_count': TrainingRecord.objects.count(),
        'deviation_count': DeviationLog.objects.count(),
        'capa_count': CapaAction.objects.count(),
        'document_count': ControlledDocument.objects.count(),
    }
    return render(request, 'main_app/dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_app:overview')
    else:
        form = AuthenticationForm()
    return render(request, 'main_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main_app:login')

def signup_view(request):
    if not request.user.is_authenticated or request.user.profile.role == 'staff':
        return redirect('main_app:overview')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role_choice = request.POST.get('role', 'staff')
            user.profile.role = role_choice
            user.profile.save()
            return redirect('main_app:overview')
    else:
        form = UserCreationForm()
    return render(request, 'main_app/signup.html', {'form': form})