from django.http import HttpResponseRedirect , HttpResponse , HttpRequest , Http404
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse #reverse function :: reverse('appname:url_name' , args=( , , ) == vorodi haye url)
from django.views import generic #baraye estefade az generic view ha
from django.utils import timezone #baraye dadan tarikh
from .models import * #import kardan hame model haye barname
from .forms import *
# Create your views here.

def base(request):
    return render(request ,'weblog/base.html', {})

def home(request):

    last_users = User.objects.order_by('-signup_date')[:10]
    last_blogposts = BlogPost.objects.order_by('-pub_date')[:10]
    return render(request ,'weblog/home.html', {'last_users' : last_users , 'last_blogposts' : last_blogposts})
    
def login(request):
    pass


def additional_info_form_view(request , username):

    #if this form didn't created by redirect from register form this should be Bad Access
    #inkaro krdm ke harkasi ke in linko balad bood nayad darja dastresi peida kone
    #etelaat melato avaz kone!

    #in karbord session dar haqiqat yek anti refreshe
    #mese safeye pardakht online ke nabayad refresh koni!

    if request.method == 'GET':
        if not request.session.get('form-submitted' , True):
            raise Http404("Bad Access Don't Refresh The Page or Try To Reach This Without Registering !") 
    additional_form = additional_info_Form()
    error_msg = ''
    request.session['form-submitted'] = False
    if request.method == 'POST':
        additional_form = additional_info_Form(request.POST)
        if additional_form.is_valid():
            print('ADDITIONAL INFO VALIDATION SUCCESS!')
            print(additional_form.cleaned_data)
            obj = User.objects.get(pk = username)
            obj.github_link = additional_form.cleaned_data['github_link']
            obj.facebook_link = additional_form.cleaned_data['facebook_link']
            obj.Linkedin_link = additional_form.cleaned_data['Linkedin_link']
            obj.Instagram_link = additional_form.cleaned_data['Instagram_link']
            obj.Telegram_link = additional_form.cleaned_data['Telegram_link']
            obj.Telegram_ID = additional_form.cleaned_data['Telegram_ID']
            obj.save()
            return render(request , 'weblog/Success.html' , {'username' : username})

        else:
            print('ADDITIONAL INFO VALIDATION FAILED')
            print(additional_form.cleaned_data)
            error_msg = 'Please Fix The Issues !'

    return render(request , 'weblog/additional_info_register.html' , {'username' : username , 'additional_form' : additional_form , 'error_msg' : error_msg})


def register_form_view(request):
    signup_form = signupForm()
    error_msg = ''
    if request.method == 'POST':
        # print(request.POST)
        signup_form = signupForm(request.POST)
        if signup_form.is_valid():
            print('REGISTER VALIDATION SUCCESS!')
            print(signup_form.cleaned_data)
            signup_form.save(commit = True)

            # addin some session for redirect restriction :: 
            request.session['form-submitted'] = True
            return HttpResponseRedirect(reverse('weblog:additional_info', args=(signup_form.cleaned_data['username'],)))
        else:
            print('REGISTER VALIDATION FAILED')
            print(signup_form.cleaned_data)
            error_msg = 'Please Fix The Issues !'
    return render(request , 'weblog/register.html' , {'signup_form' : signup_form , 'error_msg' : error_msg})

def signin_form(request):
    return HttpResponseRedirect(reverse('weblog:home', args=()))

def aboutus(request):
    return HttpResponseRedirect(reverse('weblog:home', args=()))
