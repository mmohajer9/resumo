from django.http import HttpResponseRedirect , HttpResponse , HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.

def index(request):
    return HttpResponse('This is Index Page')