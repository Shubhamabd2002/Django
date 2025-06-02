from django.urls import path
from . import views

urlpatterns = [
    path('get_todo/<uuid:id>/', views.TodoGet, name='get'),
    path('create_todo/', views.deserialize_todo_create, name='create'),
    path('update_todo/', views.update_todo, name='update'),
    path('get_all/', views.getAllList, name='get_all'),
    path('delete_todo/', views.delete_todo, name='delete')
]