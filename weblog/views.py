from django.http import HttpResponseRedirect , HttpResponse , HttpRequest
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse #reverse function :: reverse('appname:url_name' , args=( , , ) == vorodi haye url)
from django.views import generic #baraye estefade az generic view ha
from django.utils import timezone #baraye dadan tarikh
from .models import * #import kardan hame model haye barname
from .forms import *
# Create your views here.



def home(request):

    last_users = UserDetail.objects.order_by('-signup_date')[:10]
    last_blogposts = BlogPost.objects.order_by('-pub_date')[:10]
    return render(request ,'weblog/home.html', {'last_users' : last_users , 'last_blogposts' : last_blogposts})
    
def login(request):
    pass

def signup(request):
    pass

def additional_info_register_form(request):
    pass

def register_form(reuqest):
    signup_form = signupForm()
    if reuqest.method == 'POST':
        # print(reuqest.POST)
        signup_form = signupForm(reuqest.POST)
        if signup_form.is_valid():
            #DO SOMETHING
            print('VALIDATION SUCCESS!')
            print(signup_form.cleaned_data)
            signup_form.save(commit = True)
        else:
            print('VALIDATION FAILED')    
            #return render jadid baraye additional info ba ye form ezafe!
    return render(reuqest , 'weblog/register.html' , {'signup_form' : signup_form})

def signin_form(request):
    return HttpResponse('signin_form')

def aboutus(request):
    return HttpResponse('aboutus')