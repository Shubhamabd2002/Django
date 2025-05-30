from django.urls import path
from . import views
urlpatterns = [
    path('regester/', views.userRegestrition, name='user_regestritation')
]
