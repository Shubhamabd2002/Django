# Create your views here.
from django.http import JsonResponse
from django.db import IntegrityError
import json
from . import utils
from django.views.decorators.csrf import csrf_exempt
from .import serializers
from django.contrib.auth import login, logout, authenticate

@csrf_exempt
def userRegestrition(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            user = utils.createNewUser(username, email, password)
            return JsonResponse({'message': 'User registration successfull', 'user': serializers.UserRegTodo(user)}, status = 201)
        except IntegrityError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred: " + str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are supported for this endpoint."}, status=405)

@csrf_exempt
def userLoginView(request):
    if request.method == 'POST':
        try:
            logData = json.loads(request.body)
            username = logData.get('username')
            password = logData.get('password')

            if not username or not password:
                return JsonResponse({'error': 'Username and password are required.'}, status = 400)
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Login successful!'}, status = 200)
            else:
                return JsonResponse({"error": "Invalid credentials."}, status=401)
        except IntegrityError as e:
            return JsonResponse({"error": "Invalid JSON in request body." + str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred: " + str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are supported for this endpoint."}, status=405)

        
@csrf_exempt
def userLogoutView(request):
    if request.method == 'POST':
        try:
            if request.user.is_authenticated:
                logout(request)
                return JsonResponse({"message": "Logout successful!"}, status=200)
        except IntegrityError as e:
            return JsonResponse({"error": "Invalid JSON in request body." + str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred: " + str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are supported for this endpoint."}, status=405)