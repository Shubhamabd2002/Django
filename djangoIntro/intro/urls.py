from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_intro, name='all_intro'),
]
