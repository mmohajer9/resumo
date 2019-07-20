from django.http import HttpResponseRedirect , HttpResponse , HttpRequest , Http404
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse #reverse function :: reverse('appname:url_name' , args=( , , ) == vorodi haye url)
from django.views.generic import (View , TemplateView , ListView , DetailView, 
                                         CreateView , UpdateView , DeleteView )
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


class UserWallView(ListView):
    model = BlogPost
    # it will return a list context with the context name : blogpost_list so it is the default
    # now u can over ride this feature with context_object_name and changing it to what u desire
    context_object_name = 'blogposts'
    #bayad tavajoh krd ke dar har soorat context object_list besorat default ba hamin esm hamishe hast 
    #va mitoni azash estefade koni age esmi nazashti ya nakahasti az blogpost_list default estefade koni
    


    # template name is also has an default value called 'blogpost_list.html' and u can over ride this too!
    template_name='weblog/user_wall.html'
    

    # queryset is telling us that what context should send to template via context_object_name
    def get_queryset(self):
        print('from get_queryset  ---' ,self.kwargs) #chizayi ke besorat <str:username> dadi mire to kwargs besorat dictionary {'username' : value }
        return BlogPost.objects.filter(username = self.kwargs['username']).order_by('-pub_date')


    #mitoni etelaat khodeto be contexte mored nazar ezafe koni !
    def get_context_data(self, **kwargs):
        context = super(UserWallView, self).get_context_data(**kwargs)
        context['username_in_url'] = self.kwargs['username']
        for key in context:
            print(key , context[key])
        return context

class PostDetailView(DetailView):
    model = BlogPost
    template_name='weblog/post.html'
    
    # toye in chon marbot be faghat ye object az BlogPost hast va detail haye ono neshon mide pas pk = id ro az url migire
    # va motabegh id ke daryaft krde mire post marbot be on id ro barmigardone toye 2ta context mirize ke mitoni esmashono avaz koni
    # besorat default toye : object , blogpost
    # bar khalaf list ha ke toshon object_list , blogpost_list dare!


    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        for key in context:
            print(key , context[key])        
        return context

class BlogPostCreateView(CreateView):
    fields = ('title' , 'body')
    model = BlogPost
    template_name = "weblog/newpost.html"


def edit_profile(request , username):

    if request.user.username != username:
        
        raise Http404(f'Page Not Found ! You Can Not Access This Page without Login as "{username}" ')
    
    if request.method == 'POST':

        user_obj = User.objects.get_by_natural_key(username)
        profile = UserDetail.objects.get(user = user_obj)

        post = request.POST.copy()
        if post.get('is_private') == 'on':
            post['is_private'] =  1
        else:
            post['is_private'] =  0


        for i in post:
            if post[i] == 'None':
                post[i] = ''
        

        request.POST = post

        # for i in request.POST:
        #     print(i + '  ---  ',request.POST[i])

        
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']   

        profile.aboutme = request.POST['aboutme']
        profile.github_link = request.POST['github_link']
        profile.facebook_link = request.POST['facebook_link']
        profile.Linkedin_link = request.POST['Linkedin_link']
        profile.Instagram_link = request.POST['Instagram_link']
        profile.Telegram_link = request.POST['Telegram_link']
        profile.personal_website = request.POST['personal_website']
        profile.phone = request.POST['phone']
        profile.profession = request.POST['profession']
        profile.bio = request.POST['bio']
        profile.is_private = request.POST['is_private']

        if request.POST.get('clearphoto') == 'on':
            profile.profile_pic.delete(save = True)

        profile.save()
        return HttpResponseRedirect(reverse('weblog:profile'))
        
    return render(request ,'weblog/edit_profile.html' , {'username' : username}) 

def user_profile(request , username):

    user_obj = User.objects.get_by_natural_key(username)


    if user_obj.userdetail.is_private and str(user_obj.username) != str(request.user.username):
        raise Http404('This Page Is Private')
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


