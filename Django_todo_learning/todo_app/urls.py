from django.urls import path
from . import views

urlpatterns = [
    path('add-todo/', views.TodoCreateViews.as_view(), name='add-todo-list'),
    path('get-list/', views.TodoGetViews.as_view(), name='get-todo-list')
]
