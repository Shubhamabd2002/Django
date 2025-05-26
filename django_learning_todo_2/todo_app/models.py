from django.db import models
from uuid import uuid4

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid4, primary_key=True)

    def __str__(self):
        return self.title
