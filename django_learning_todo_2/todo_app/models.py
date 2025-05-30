from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view_all_todo", "can view all todo item"),
            ("can_manage_all_todo", "can update, delete and create todo item"),
        ]
    def __str__(self):
        return self.title
