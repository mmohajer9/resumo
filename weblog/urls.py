from django.urls import path , include
from . import views

app_name = 'weblog'

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('register/' , views.register_form_view , name = 'register'),
    path('register/additional/<str:username>/' , views.additional_info_form_view , name = 'additional_info'),
    path('signin/' , views.signin , name = 'signin'),
    path('aboutus/',views.aboutus , name = 'aboutus'),
    path('signout/' , views.signout , name = 'signout'),
    path('profile/<str:username>/' , views.user_profile , name = 'user_profile'),
    path('profile/' , views.profile , name = 'profile'),
    path('base/' , views.base , name = 'base'),
    # path('profile/<str:username>/newpost' , views.newpost , name = 'newpost'),
    # path('profile/<str:username>/wall' , views.wall , name = 'wall'),
    # path('profile/<str:username>/edit_profile' , views.edit_profile , name = 'edit_profile'),
    # path('profile/<str:username>/edit_user' , views.edit_user , name = 'edit_user'),
    # -- I Should Think ! -- #
]   
