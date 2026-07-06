from django.urls import path
from . import views 

app_name = 'main_app'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.overview_dashboard, name='overview'),
]