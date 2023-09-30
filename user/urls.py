from django.urls import path
from . import views,profile


urlpatterns = [
    path('user/', views.UserCreate.as_view(), name='user-create'), 
    path('profile/', profile.profile, name='profile'),
    path('profile/<str:username>/', profile.profile, name='profile-detail'),
]