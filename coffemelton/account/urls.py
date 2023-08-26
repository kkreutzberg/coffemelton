from django.urls import path
from . import views

# app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile-management/', views.profile_management, name='profile-management'),
    path('delete-account/', views.delete_account, name='delete-account'),
]
