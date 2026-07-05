from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    
    return HttpResponse('<h1>Hello!</h1>')

def about(request):
    
    return render(request, 'main_app/about.html')

def overview_dashboard(request):
    
    return render(request, 'main_app/dashboard.html')
