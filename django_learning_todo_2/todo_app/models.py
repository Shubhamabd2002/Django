from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Todo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    due_date = models.DateField()

    @property
    def is_overdue(self):
        return datetime.date.today() >= self.due_date


    # class Meta:
    #     permissions = [
    #         ("can_view_all_todo", "can view all todo item"),
    #         ("can_manage_all_todo", "can update, delete and create todo item"),
    #     ]
    def __str__(self):
        return self.title
