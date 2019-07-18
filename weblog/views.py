from django.http import HttpResponseRedirect , HttpResponse , HttpRequest , Http404
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse #reverse function :: reverse('appname:url_name' , args=( , , ) == vorodi haye url)
from django.views import generic #baraye estefade az generic view ha
from django.utils import timezone #baraye dadan tarikh
from .models import * #import kardan hame model haye barname
from .forms import *

from django.core.exceptions import ObjectDoesNotExist

from online_users.models import OnlineUserActivity , timedelta

from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# def base(request):
#     return render(request ,'weblog/base.html', {})


def edit_profile(request , username):
    return render(request ,'weblog/edit_profile.html' , {'username' : username}) 

def user_profile(request , username):

    user_obj = User.objects.get_by_natural_key(username)


    if user_obj.userdetail.is_private:
        return Http404('This Page Is Private')
    else:

        return render(request ,'weblog/user_profile.html', {'user_obj' : user_obj , 'username_in_url' : username}) 


def profile(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('weblog:user_profile' , args=(request.user,)))
    else:
        return HttpResponseRedirect(reverse('weblog:signin' , args=()))

def home(request):

    online_users = OnlineUserActivity.get_user_activities(timedelta(seconds=30))

    last_users = User.objects.order_by('-signup_date')[:10]
    last_blogposts = BlogPost.objects.order_by('-pub_date')[:10]
    return render(request ,'weblog/home.html', {'last_users' : last_users , 'last_blogposts' : last_blogposts , 'online_users' : online_users})

@login_required
def signout(request):
    logout(request)
    return render(request ,'weblog/logoutSuccessful.html', {})



def signin(request):

    if request.user.is_authenticated:
        print(request.user)
        return HttpResponseRedirect(reverse('weblog:home', args=()))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)
        
        if user:
            if user.is_active:
                login(request , user)
                return render(request ,'weblog/loginSuccessful.html', {})
            
            else:
                error_msg = 'حساب شما مسدود است برای اطلاعات بیشتر با مدیریت تماس بگیرید'
                return render(request ,'weblog/error.html', {'error_msg' : error_msg})

        else:
            print("Login Failed !")
            print(f"Username: {username} and Password: {password}")

            error_msg = 'نام کاربری یا رمز عبور شما اشتباه است'

            return render(request ,'weblog/error.html', {'error_msg' : error_msg})

    else:

        return render(request , 'weblog/signin.html' , {})

def additional_info_form_view(request , username):

    #if this form didn't created by redirect from register form this should be Bad Access
    #inkaro krdm ke harkasi ke in linko balad bood nayad darja dastresi peida kone
    #etelaat melato avaz kone!

    #in karbord session dar haqiqat yek anti refreshe
    #mese safeye pardakht online ke nabayad refresh koni!
    



    if request.method == 'GET':
        #if not request.session.get('form-submitted' , True): #TYPE 1
        if not 'form-submitted' in request.session: #TYPE 2
            raise Http404("Bad Access Don't Refresh The Page or Try To Reach This Without Registering !") 
        del request.session['form-submitted']

    additional_form = additional_info_Form()
    error_msg = ''
        
    
    if request.method == 'POST':
        additional_form = additional_info_Form(data = request.POST , files = request.FILES)
        if additional_form.is_valid():
            print('ADDITIONAL INFO VALIDATION SUCCESS!')
            print(additional_form.cleaned_data)
            user = User.objects.get(pk = username)
            profile = additional_form.save(commit = False) # Object az noe model UserDetial Bar migardone !
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            return render(request , 'weblog/registerSuccess.html' , {'username' : username})

        else:
            print('ADDITIONAL INFO VALIDATION FAILED')
            print(additional_form.cleaned_data)
            error_msg = 'Please Fix The Issues !'

    return render(request , 'weblog/additional_info_register.html' , {'username' : username , 'additional_form' : additional_form , 'error_msg' : error_msg})


def register_form_view(request):
    signup_form = signupForm()
    error_msg = ''

    if request.user.is_authenticated:
        print(request.session)
        return HttpResponseRedirect(reverse('weblog:home', args=()))

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


def aboutus(request):
    return HttpResponseRedirect(reverse('weblog:home', args=()))


