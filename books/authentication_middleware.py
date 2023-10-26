from django.shortcuts import redirect
from django.urls import resolve

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print(request.path)
        if not request.user.is_authenticated and resolve(request.path).url_name != 'login':
            return redirect('login')

        return self.get_response(request)


