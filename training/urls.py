from django.urls import path
from . import views

app_name = 'training'

urlpatterns = [
    path('', views.training_dashboard, name='dashboard'),
    path('create/', views.training_create, name='create'),
    path('<int:pk>', views.training_detail, name='detail'),
    path('<int:pk>/edit/', views.training_update, name='edit'),
    path('<int:pk>/delete/', views.training_delete, name='delete'),
]
