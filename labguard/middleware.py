from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path.startswith('/admin/'):
            return self.get_response(request)
        
        if not request.user.is_authenticated:
            
            allowed_urls = [
                reverse('main_app:login'),
                reverse('main_app:signup'),
                reverse('main_app:about'),
            ]
            
            if request.path not in allowed_urls:
                return redirect('main_app:login')
            
        return self.get_response(request)