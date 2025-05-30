# Create your views here.
from django.http import JsonResponse
from django.db import IntegrityError
import json
from . import utils
from django.views.decorators.csrf import csrf_exempt
from .import serializers

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
