from django.http import JsonResponse
from functools import wraps

def login_req_api(func):
    @wraps(func)
    def wrapper( request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required. Please log in.'}, status=401)
        return func(request, *args, **kwargs)
    return wrapper
