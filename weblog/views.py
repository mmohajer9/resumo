from django.http import HttpResponseRedirect , HttpResponse , HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import *
# Create your views here.



def index(request):

    users = UserDetail.objects.all()
    
    return render(request ,'weblog/index.html', {'users' : users})