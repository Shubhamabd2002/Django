from django.db import models
from uuid import uuid4

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid4, primary_key=True)

    class Meta:
        permissions = [
            ("can_view_all_todo", "can view all todo item"),
            ("can_manage_all_todo", "can update, delete and create todo item"),
        ]
    def __str__(self):
        return self.title
