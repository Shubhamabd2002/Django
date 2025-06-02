from . import models
from . import serializers
from django.http import JsonResponse, HttpResponseBadRequest
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .decorator import login_req_api
from django.db import connection
from pprint import pprint
from django.utils import timezone
import datetime

# Create your views here.
@login_req_api
def getAllList(request):
    todo = models.Todo.objects.select_related("user").filter(user = request.user)
    data = serializers.TodoSerializers(todo, many=True)
    pprint(connection.queries)
    
    return JsonResponse({'data': data},status = 201)

@login_req_api
def TodoGet(request, id):
    try:
        todo = models.Todo.objects.get(id=id)
        serialized_data = serializers.TodoSerializers(todo)
        return JsonResponse(serialized_data)
    except models.Todo.DoesNotExist:
        return JsonResponse({'error': 'todo not found'}, status = 404)
    
@login_req_api
@csrf_exempt
def deserialize_todo_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data, '23456')
            title =  data.get('title')

            if not title:
                return JsonResponse({'error': 'title is required field'}, status = 404)
            try:
                todo = models.Todo(
                    title = title,
                    user = request.user,
                    due_date = datetime.date.today()
                )
                print(todo, 'todo instance')
                todo.save()

                serializers_data = serializers.TodoSerializers(todo)
                print(serializers_data, 'todo instance')
                return JsonResponse(serializers_data, status = 201)
            except:
                return JsonResponse({'error': 'Invalid data', 'data': data}, status = 400)
        except:
            return JsonResponse({'error': 'Invalid data 123'}, status = 400)
    else:
        return JsonResponse({'error': 'Invalid data 123456'}, status = 400)

@login_req_api
@csrf_exempt
def update_todo(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            selectedTodo = models.Todo.objects.get(id = data.get('id'))
            if selectedTodo:
                selectedTodo.title = data.get('title')
                selectedTodo.save()
                return JsonResponse({'message': 'Product updated', 'id': selectedTodo.id}, status = 201)
            else:
                return JsonResponse({'error': 'Invalid data', 'data': data}, status = 400)
        except models.Todo.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    else: 
        return HttpResponseBadRequest("Only PUT method allowed.")

@login_req_api 
@csrf_exempt #CSRF (Cross-Site Request Forgery) is a security vulnerability that allows an attacker to perform actions on behalf of a logged-in user without their consent.
def delete_todo(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        try:
            selectedTodo = models.Todo.objects.get(id = data.get('id'))
            if selectedTodo:
                selectedTodo.delete()
                return JsonResponse({'message': 'Product Deleted', 'updatedData': serializers.TodoSerializers(models.Todo.objects.all(), many=True)}, status = 201)
            else:
                return JsonResponse({'error': 'Invalid data', 'data': data}, status = 400)
        except models.Todo.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    else: 
        return HttpResponseBadRequest("Only PUT method allowed.")
