def UserRegTodo(user_instance):
    return {
        'id': user_instance.id,
        'username': user_instance.username,
        'email': user_instance.email,
        'date_joined': user_instance.date_joined,
        'password': user_instance.password,
    }