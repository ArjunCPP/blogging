from unicodedata import name
from django.urls import path,include
from . import views 
from users import views as user_views
urlpatterns = [
path('',views.home,name='blog-home'),
path('about/',views.about,name='blog-about'),
path('register/',user_views.register,name='register'),
]