from django.urls import path , include
from . import views

app_name = 'weblog'

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('register/' , views.register_form , name = 'register'),
    path('signin/' , views.signin_form , name = 'signin'),
    path('aboutus/',views.aboutus , name = 'aboutus')
    
]   
