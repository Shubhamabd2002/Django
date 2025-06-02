import datetime

def TodoSerializers(todo_queryset, many=False):
    if many:
        return [{
            'title': todo.title,
            'id': todo.id,
            'user': todo.user.id,
            'due_date': todo.due_date,
            'is_overdue': todo.is_overdue,
        } for todo in todo_queryset]
            
    else:
        return {
            'title': todo_queryset.title,
            'id': todo_queryset.id,
            'user': todo_queryset.user.id,
            'due_date': todo_queryset.due_date,
            'is_overdue': todo_queryset.is_overdue,
        }
