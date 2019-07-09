from django.urls import path , include
from . import views

app_name = 'weblog'

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('authentication/' , views.authentication , name = 'authentication'),
    path('login/' , views.login , name = 'login'),
    path('signup/' , views.signup , name = 'signup'),
    
]   
