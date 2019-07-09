from django.http import HttpResponseRedirect , HttpResponse , HttpRequest
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse #reverse function :: reverse('appname:url_name' , args=( , , ) == vorodi haye url)
from django.views import generic #baraye estefade az generic view ha
from django.utils import timezone #baraye dadan tarikh
from .models import * #import kardan hame model haye barname
# Create your views here.



def home(request):

    last_users = UserDetail.objects.order_by('signup_date')[:10]
    last_blogposts = BlogPost.objects.order_by('pub_date')[:10]
    return render(request ,'weblog/home.html', {'last_users' : last_users , 'last_blogposts' : last_blogposts})


def authentication(reuqest):
    return render(reuqest , 'weblog/authentication.html')


def login(request):
    pass

def signup(request):
    pass