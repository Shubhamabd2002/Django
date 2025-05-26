
from . import models

def TodoSerializers(todo_instance):
    return {
        'title': todo_instance.title,
        'id': todo_instance.id,
    }

def serialize_todo_list(todo_queryset):
    return [TodoSerializers(todo) for todo in todo_queryset]