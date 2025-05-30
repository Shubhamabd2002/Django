from django.db import models
from django.core.validators import RegexValidator
from uuid import uuid4
# Create your models here.

# password_validator = RegexValidator(
#     regex='^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
#     message="Password must contain at least 8 characters, one letter, one number, and one special character."
# )
class UserRegTodo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username