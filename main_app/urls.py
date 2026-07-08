from django.urls import path
from . import views 

app_name = 'main_app'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.overview_dashboard, name='overview'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]