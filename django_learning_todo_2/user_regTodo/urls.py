from django.urls import path
from . import views
urlpatterns = [
    path('regester/', views.userRegestrition, name='user_regestritation'),
    path('login/', views.userLoginView, name='user_login'),
    path('logout/', views.userLogoutView, name='user_logout'),
]
