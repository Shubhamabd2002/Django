from django.contrib.auth.models import User
from django.db import IntegrityError

def createNewUser(username, email, password):
    try:
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password,
        )
        return user
    except IntegrityError as e:
        raise IntegrityError(f"A user with that username or email already exists: {e}")
    except Exception as e:
        raise Exception(f"Failed to create user: {e}")
    
    
    
    