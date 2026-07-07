from django.urls import path
from . import views

app_name = 'capas'

urlpatterns = [
    path('', views.capa_dashboard, name='dashboard'),
    path('create/', views.capa_create, name='create'),
    path('<int:pk>/', views.capa_detail, name='detail'),
    path('<int:pk>/edit/', views.capa_update, name='edit'),
    path('<int:pk>/delete/', views.capa_delete, name='delete'),
]
