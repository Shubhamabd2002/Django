from . import models
from . import serializers
from django.http import JsonResponse, HttpResponseBadRequest
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def TodoGet(request, id):
    try:
        todo = models.Todo.objects.get(id=id)
        serialized_data = serializers.TodoSerializers(todo)
        return JsonResponse(serialized_data)
    except models.Todo.DoesNotExist:
        return JsonResponse({'error': 'todo not found'}, status = 404)
    
@csrf_exempt
def deserialize_todo_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title =  data.get('title')

            if not title:
                return JsonResponse({'error': 'title is required field'}, status = 404)
            try:
                todo = models.Todo(title = title)
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

@csrf_exempt #CSRF (Cross-Site Request Forgery) is a security vulnerability that allows an attacker to perform actions on behalf of a logged-in user without their consent.
def delete_todo(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        try:
            selectedTodo = models.Todo.objects.get(id = data.get('id'))
            if selectedTodo:
                selectedTodo.delete()
                return JsonResponse({'message': 'Product Deleted', 'updatedData': serializers.serialize_todo_list(models.Todo.objects.all())}, status = 201)
            else:
                return JsonResponse({'error': 'Invalid data', 'data': data}, status = 400)
        except models.Todo.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    else: 
        return HttpResponseBadRequest("Only PUT method allowed.")
