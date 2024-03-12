from django.urls import path 
from .views import *
from knox import views as knox_views
urlpatterns = [
    path('register/',register_api),
    path('login/',login_api),
    path('user/',get_user_data),
    path('logout/',knox_views.LogoutView.as_view()),
    path('logout/',knox_views.LogoutAllView.as_view()),
    
]
