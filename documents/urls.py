from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
   path('', views.document_dashboard, name='dashboard'),
   path('create/', views.document_create, name='create'),
   path('<int:pk>/', views.document_detail, name='detail'),
   path('<int:pk>/edit/', views.document_update, name='edit'),
   path('<int:pk>/delete/', views.document_delete, name='delete'),
   ]
