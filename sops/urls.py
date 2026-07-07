from django.urls import path
from . import views

app_name = 'sops'

urlpatterns = [
    path('', views.sop_dashboard, name='dashboard'),
    path('create/', views.sop_create, name='create'),
    path('<int:pk>/', views.sop_detail, name='detail'),
    path('<int:pk>/edit/', views.sop_update, name='edit'),
    path('<int:pk>/delete', views.sop_delete, name='delete'),
]
