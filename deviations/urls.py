from django.urls import path
from . import views

app_name = 'deviations'

urlpatterns = [
    path('', views.deviation_dashboard, name='dashboard'),
    path('create/', views.deviation_create, name='create'),
    path('<int:pk>/', views.deviation_detail, name='detail'),
    path('<int:pk>/edit/', views.deviation_update, name='edit'),
    path('<int:pk>/delete/', views.deviation_delete, name='delete'),
]
