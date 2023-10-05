from django.urls import path,re_path
from . import views,profile


urlpatterns = [
    path('', views.UserCreate.as_view(), name='user-create'), 
    path('id/<int:userid>/', views.apidetails, name='apidetails'),
    path('example/<str:api_key>/', views.example_view, name='example'),
    path('profile/', profile.profile, name='profile'),
    path('profile/<str:username>/', profile.profile, name='profile-detail'),
    

    # re_path(r'^userdetail/$', views.example_view, name='example'),
    re_path(r'^userdetail/(?P<userid>\d+)/$', views.example_view, name='userdetail'),
]