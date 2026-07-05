from django.urls import path
from . import views

app_name = 'deviations'

urlpatterns = [
    path('', views.deviation_dashboard, name='dashboard'),
]
