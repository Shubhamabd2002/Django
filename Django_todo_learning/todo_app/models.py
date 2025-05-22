from django.db import models
from uuid import uuid4

class Todo(models.Model):
    text = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid4)

    def __str__(self):
        return self.text