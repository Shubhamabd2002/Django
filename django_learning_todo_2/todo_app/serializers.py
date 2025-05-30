
from . import models
from user_regTodo.serializers import UserRegTodo

def TodoSerializers(todo_instance):
    return {
        'title': todo_instance.title,
        'id': todo_instance.id,
        'user': UserRegTodo(todo_instance.user) if todo_instance.user else None
    }

def serialize_todo_list(todo_queryset):
    return [TodoSerializers(todo) for todo in todo_queryset]