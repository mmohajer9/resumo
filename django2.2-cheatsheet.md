# Django 2.2  Cheat Sheet

Here is the cheat sheet to fast developing a project in django 2.2

## Creating Virtual Environment

    mkdir sample-project-virtaulenv
    cd sample-project-virtaulenv
    virtualenv -p python3 .
    source bin/activate #it will activate your project virtualenv
    pip install django #NOTE :it will download the latest version
    (Optional) pip install django==2.2.2
    pip install pillow
    pip install django-simple-captcha
    pip install django-online-users
    pip install bcrypt
    pip install django[argon2]
    pip install humanize
    

Now it will create some folders like :
bin , include , lib , share
## Creating and Configuring Project

    cd sample-project
    django-admin startproject [PROJECT_NAME]
it will make a PROJECT_NAME folder
You Can Change its name anyway
it contains two files:

 - manage. py
 - PROJECT_NAME
	 - _ _ init_ _.py
	 - settings . py
	 - urls . py
	 - wsgi . py

   

## Creating a new app for Project (Philosophy)

> A Django Project Can Contains many apps for example : 
> You have a Social Network Project
> this project can have multiple and various apps like
> weblog  cms app , chat app , open api and .....
> so its what we are going to do:


Type in terminal:

    python3 manage.py startapp [APP_NAME]
   
it will create the app folder for You

so your folder is now sth like this:

 - PROJECT_NAME
	 - PROJECT_NAME
		 - _ _ init_ _.py
		 - settings . py
		 - urls . py
		 - wsgi . py
	 - manage .py
	 - APP_NAME
		 -	__ init __ .py
		 -	admin .py
		 -	aps .py
		 -	models .py
		 -	tests .py
		 -	views .py

Now You should add some files to APP_NAME folder its good to have these files too!

> folder : static
> folder : templates
> folder : templatetags
> folder : middleware
> file : urls .py
> file : forms .py



## Configuring Settings .py

first of all You need to add your application to project settings
so go to APP_NAME and apps .py and You see a python class with a name :

	from django.apps import AppConfig
	
    class APP_NAMEConfig(Appconfig):
	    name = 'APP_NAME'

You just simply this class i mean full location of this class to the settings .py in INSTALLED_APPS in a string:

You Also add other applications by this method too !
and the django third party packages that should be installed!
so in settings .py we have something like this :

    INSTALLED_APPS = [
    
		    'APP_NAME.apps.APP_NAMEConfig',

		    'django.contrib.admin',
		    
		    'django.contrib.auth',
		    
		    'django.contrib.contenttypes',
		    
		    'django.contrib.sessions',
		    
		    'django.contrib.messages',
		    
		    'django.contrib.staticfiles',
		    
		    'django.contrib.humanize',
		    
		    'captcha',
		    
		    'online_users',
		    
	    ]
	    

Now You should add another settings about template directory ,static files and media files

Ok! import this codes to settings .py it will set a variable that stores the correct directory for django project :

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    
    MEDIA_DIR = os.path.join(BASE_DIR , 'media')



## Configuring Templates and Static and Media

        TEMPLATES = [
    
	    {
    
		    'BACKEND': 'django.template.backends.django.DjangoTemplates',
		    
		    'DIRS': [TEMPLATE_DIR],
		    
		    'APP_DIRS': True,
		    
		    'OPTIONS': {
		    
			    'context_processors': [
			    
			    'django.template.context_processors.debug',
			    
			    'django.template.context_processors.request',
			    
			    'django.contrib.auth.context_processors.auth',
			    
			    'django.contrib.messages.context_processors.messages',
    
			    ],
    
		    },
    
	    },
    
    ]

    STATIC_URL =  '/static/'
    
    STAITCFILES_DIRS = [
    
		    STATIC_DIR,
    
	    ]
    
      
    
    
    
    MEDIA_ROOT = MEDIA_DIR
    
    MEDIA_URL =  '/media/'
    
      
      
    
    LOGIN_URL =  '/weblog/signin'

## Configuring Database Settings

    DATABASES = {
    
		    'default': {
		    
			    'ENGINE': 'django.db.backends.postgresql', 
			    #forExample for postgresql db
			    
			    'NAME': 'DATABASE_NAME',
			    
			    'USER': 'DATABASE_SERVER_USERNAME',
			    
			    'PASSWORD': 'DATABASE_SERVER_PASSWORD',
			    
			    'HOST': '127.0.0.1', 'e.g'
			    
			    'PORT': '5432', 'e.g'
	    }
    
    }

## Password Hashers and Validators


    PASSWORD_HASHERS = [
    
      
    
	    'django.contrib.auth.hashers.Argon2PasswordHasher',
	    
	    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
	    
	    'django.contrib.auth.hashers.BCryptPasswordHasher',
	    
	    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
	    
	    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    
    ]
    
    AUTH_PASSWORD_VALIDATORS = [
    
	    {
	    
		    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
		    
	    },
	    
	    {
	    
		    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
		    
		    'OPTIONS': {'min_length' : 6},
	    
	    },
    
	    {
	    
		    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	    
	    },
    
	    {
	    
		    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	    
	    },
    
    ]

## Configuring URLs

> Ok Now You Should add APP_NAME.urls.py into your primary project url folder
in urls .p in PROJECT_NAME folder in the same directory as manage .py go into it 
and change urls .py like this


    from django.contrib import admin
    
    from django.urls import path , include
    
    from APP_NAME import views
    
    from django.conf import settings
    
    from django.conf.urls.static import static
    
      
    
    urlpatterns = [
    
	    path('admin/', admin.site.urls),
	    
	    path('weblog/' , include('APP_NAME.urls')),
	    
	    path('captcha/', include('captcha.urls')),
    
    ] 	+ 	static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



Now In Your APP_NAME/urls. py insert


    from django.urls import path , include
    
    from . import views
    
      
    
    app_name =  'weblog'


	urlpatterns = [
	]



OK Your Project is almost ready to Go!


## Create Media Folder in The Same Directory as manage .py

 - PROJECT_NAME(Can be Change)
	 - manage .py
	 - PROJECT_NAME
	 - APP_NAME
	 - media



## Namespacing The Project

In Our Project we could have as many as we want apps!
so its very important to have namespace for every apps in this project

make a folder with the name : 'APP_NAME'

in every static , media , templates and we will refrence them by calling the app name first of all url and paths!

# Important Notes!

### This Notes are From my Project 'Resumo'


## Django Forms and ModelForms  and is_valid() function

Forms are simple !

.
.

Model Form Type:
    
    class  signupForm(forms.ModelForm):
    
	    verifyEmail = forms.EmailField(label='Verify Your Email')
	    
	    botcatcher = forms.CharField(required=False , widget  = forms.HiddenInput , validators=[validators.MaxLengthValidator(0)])
	    
	    captcha = CaptchaField()
	    
	    class  Meta:
	    
		    model = User
		    
		    fields = ('username' , 'password' , 'firstname' , 'lastname' , 'email' ,)
		    
		    widgets = {
		    
			    'password' : forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
			    
			    'username' : forms.TextInput(attrs={'placeholder': 'Enter Username'}),
			    
			    'firstname' : forms.TextInput(attrs={'placeholder': 'e.g. Mohammad'}),
			    
			    'lastname' : forms.TextInput(attrs={'placeholder': 'e.g. Ahmadi'}),
			    
			    'email' : forms.EmailInput(attrs={'placeholder': 'test@test.com'}),
		    
		    }
    
	    def  clean_botcatcher(self):
	    
		    print('form method of clean_botcatcher called')
		    
		    botcatcher =  self.cleaned_data['botcatcher']
		    
		    if  len(botcatcher) >  0:
		    
			    raise forms.ValidationError('BOT Caputured!')
	    
      
    
		    return botcatcher
    
      
    
	    def  clean_verifyEmail(self):
	    
		    print('form method of verifyMail called')
		    
		    email =  self.cleaned_data['email']
		    
		    verifyEmail =  self.cleaned_data['verifyEmail']
	    
      
    
		    if email != verifyEmail:
		    
			    raise forms.ValidationError('Emails Are not Match Together')
			    
		    return verifyEmail
    
      
      
      
    
	    #save bayad override bshe! chon hash nadare save ghabli
	    
	    def  save(self, commit  =  True):
	    
		    user =  super().save(commit  =  False) # Call the real save() method
		    
		    user.set_password(self.cleaned_data['password'])
		    
		    if(commit):
		    
			    user.save()
		    
		    return user


There are some notes about this model form :

 ### 1 - If u want to use django authentication and this model form is some how related to django auth 
 
 ###  like in this example that is our user that is using django auth model  You should over ride save method
 ###  for this form just like what i have done !



###  2 - When You Call is_valid() in Your Views there are some actions that happened behind:

>  1. clean Method Called
>  2. clean_fieldname called
> 
> in clean method there are 3 works that will be done :
> 1 - converting all field values in the form and its template to python valid Data Types to read them
> 2 - put valid fields in the form.cleaned_data dict and throw away unvalid datas
> 3 - if we didnt have any unvalid datas so is_valid is true then it will return True unless it will return False


## Models and Using Django Authentication Model for Connecting Django Authentication system to our Customized User Model or Extended User Model

First of all check this imports :

    from django.db import models
    
    from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

Two Base Models Should Be Inherited and over ride again! 
1 - AbstractBaseUser
2 - BaseUserManager in a Composite in First One





    class  UserManager(BaseUserManager):
	    
	    def  create_user(self , username , email , password  =  None , is_active  =  True , is_staff  =  False , is_admin  =  False):
	    
		    if  not username:
		    
			    raise  ValueError("Users Must Have a Username")
		    
		    if  not email:
		    
			    raise  ValueError("Users Must Have an Email")
		    
		    if  not password:
		    
			    raise  ValueError("Users Must Have a Password")
	    
	      
	    
		    user_obj =  self.model(
		    
			    email  =  self.normalize_email(email),
			    
			    username  = username,
		    
		    )
	    
		    user_obj.set_password(password) # change user password
		    
		    user_obj.staff = is_staff
		    
		    user_obj.admin = is_admin
		    
		    user_obj.active = is_active
		    
		    user_obj.save(using  =  self._db)
		    
		    return user_obj
		    
	      
	    
	    def  create_staffuser(self , username , email , password  =  None):
	    
		    user =  self.create_user(
		    
		    username,
		    
		    email,
		    
		    password  = password,
		    
		    is_staff  =  True
	    
		    )
	    
		    return user
	    
	      
	    
	    def  create_superuser(self , username , email , password  =  None):
	    
		    user =  self.create_user(
		    
		    username,
		    
		    email,
		    
		    password  = password,
		    
		    is_staff  =  True,
		    
		    is_admin  =  True
		    
		    )
	    
		    return user







    class  User(AbstractBaseUser):
    
      
    
	    username = models.CharField(max_length=50 , primary_key  =  True , unique  =  True)
	    
	    email = models.EmailField(max_length=254 , unique  =  True , default  =  'test@test.com')
	    
	    firstname = models.CharField(max_length=50)
	    
	    lastname = models.CharField(max_length=50)
	    
	    active = models.BooleanField(default  =  True)
	    
	    staff = models.BooleanField(default  =  False)
	    
	    admin = models.BooleanField(default  =  False)
	    
	    signup_date = models.DateTimeField(auto_now_add  =  True)
    
      
	      
	    
	    USERNAME_FIELD =  'username'
	    
	      
	    
	    REQUIRED_FIELDS = ['email']
	    
	      
	    
	    objects = UserManager()
	    
	      
	    
	    def  __str__(self):
	    
		    return  self.username
	    
	      
	    
	    def  get_full_name(self):
	    
		    return  self.firstname +  ' '  +  self.lastname
	    
	      
	    
	    def  get_short_name(self):
	    
		    return  self.firstname
		    
	      
	    
	    def  has_perm(self , perm , obj  =  None):
	    
		    return  True
	    
	      
	    
	    def  has_module_perms(self , app_label):
	    
		    return  True
	    
	      
	    
	    @property
	    
	    def  is_staff(self):
	    
		    return  self.staff
	    
	      
	    
	    @property
	    
	    def  is_admin(self):
	    
		    return  self.admin
	    
	    @property
	    
	    def  is_active(self):
	    
		    return  self.active

## About Request


> in Function Views  request is a kind of Httprequest Object from django.http
> that is going through parameter
> .
> 
> in Class Based Views You Can Access To it in functions with self.request
> .
> You Should Pass other url parameters as the parameters of a function
> example:

if URL pattern is weblog/<str:username >/<int:postid >

Your Function view should be :

> def SomeView(request , username , postid):
	>

in Class Based Views We Should access to username and post id via self.kwargs ['username'] and self.kwargs['postid]


## My Views


    class  UserWallView(ListView):
    
	    model = BlogPost
	    
	    # it will return a list context with the context name : blogpost_list so it is the default
	    
	    # now u can over ride this feature with context_object_name and changing it to what u desire
	    
	    context_object_name =  'blogposts'
	    
	    #bayad tavajoh krd ke dar har soorat context object_list besorat default ba hamin esm hamishe hast
	    
	    #va mitoni azash estefade koni age esmi nazashti ya nakahasti az blogpost_list default estefade koni
	    
	      
	      
	    
	    # template name is also has an default value called 'blogpost_list.html' and u can over ride this too!
	    
	    template_name='weblog/user_wall.html'
	    
	      
	    
	    # queryset is telling us that what context should send to template via context_object_name
	    
	    def  get_queryset(self):
	    
		    # print('from get_queryset ---' ,self.kwargs) #chizayi ke besorat <str:username> dadi mire to kwargs besorat dictionary {'username' : value }
	    
		    return BlogPost.objects.filter(username  =  self.kwargs['username']).order_by('-pub_date')
	    
	      
	      
	      
	    
	    #mitoni etelaat khodeto be contexte mored nazar ezafe koni !
	    
	    def  get_context_data(self, **kwargs):
	    
		    context =  super(UserWallView, self).get_context_data(**kwargs)
	    
		    context['username_in_url'] =  self.kwargs['username']
	    
		    # for key in context:
	    
			    # print(key , context[key])
	    
		    return context
	    
	      
	    
    class  PostDetailView(DetailView):
	    
	    model = BlogPost
	    
	    template_name='weblog/post.html'
	    
	    # toye in chon marbot be faghat ye object az BlogPost hast va detail haye ono neshon mide pas pk = id ro az url migire
	    
	    # va motabegh id ke daryaft krde mire post marbot be on id ro barmigardone toye 2ta context mirize ke mitoni esmashono avaz koni
	    
	    # besorat default toye : object , blogpost
	    
	    # bar khalaf list ha ke toshon object_list , blogpost_list dare!
	    
	      
	    
	    def  get_context_data(self, **kwargs):
	    
		    context =  super(PostDetailView, self).get_context_data(**kwargs)
	    
		    if  self.request.user.is_authenticated:
	    
		    if BlogPostLike.objects.filter(blogPost_id  = context['object']).filter(username  =  self.request.user).exists():
	    
			    auth_user_like = BlogPostLike.objects.filter(blogPost_id  = context['object']).get(username  =  self.request.user)
	    
		    context['auth_user_like'] = auth_user_like
	    
		    for key in context:
	    
			    print(key , context[key])
	    
		    return context
	    
	      
	    
	    def  post(self , request , *args, **kwargs):
	    
		    if  self.request.user.is_authenticated:
	    
			    try:
	    
				    bp = BlogPost.objects.get(pk  =  self.kwargs['pk'])
	    
				    cm = bp.comment_set.get_or_create(username  = request.user , comment_text  = request.POST['comment_text'])
	    
				    return HttpResponseRedirect(reverse('weblog:post' , args=(self.kwargs['username'] , self.kwargs['pk'])))
	    
			    except:
	    
				    return HttpResponseRedirect(reverse('weblog:post' , args=(self.kwargs['username'] , self.kwargs['pk'])))
	    
	      
	    
		    else:
			    
			    raise Http404('Bad Access ! Please Log In')
		    
	      
	    
	    # in function baraye gereftan object e ke toe context hast besorat default pk ro az url bar midare va on object ro bar migardone
	    
	    # ye halat ham copy az on doros mikone mirize to blogpost
	    
	    # def get_object(self, queryset=None):
	    
	    # return super().get_object(queryset=queryset)
    
      
    
    class  PostLikeListView(ListView):
    
	    model = BlogPostLike
	    
	    context_object_name =  'likes'
	    
	    template_name='weblog/postlike.html'
	    
	      
	      
	    
	    def  get_queryset(self):
	    
		    return BlogPostLike.objects.filter(blogPost_id  =  self.kwargs['pk'])
	    
	      
	    
	    def  get_context_data(self, **kwargs):
	    
		    context =  super(PostLikeListView, self).get_context_data(**kwargs)
	    
		    context['username_in_url'] =  self.kwargs['username']
	    
		    context['post_title'] = BlogPost.objects.filter(id  =  self.kwargs['pk']).values_list('title' , flat  =  True)[0]
	    
		    context['post_id'] =  self.kwargs['pk']
	    
		    # for key in context:
	    
			    # print(key , context[key])
	    
		    return context
	    
      
      
      
    
    class  PostCreateView(CreateView):
    
	    fields = ('title' , 'body' , 'post_pic')
	    
	    model = BlogPost
	    
	    template_name =  "weblog/newpost.html"
	    
	      
	    
	    #chizi ke ina be onvan context montaqel mikonan contexti bename form hast ke toye template azash estefade krdm
	    
	      
	    
	    def  form_valid(self, form):
	    
		    if  self.request.user.is_authenticated and  self.request.user.username ==  self.kwargs['username']:
	    
			    user_obj = get_object_or_404(User , username  =  self.kwargs['username'])
	    
			    form.instance.username = user_obj
	    
			    print(form.instance) #an instance of BlogPost! before saving to database and setting a pk (id)
	    
			    return  super().form_valid(form)
	    
		    else:
	    
			    raise Http404('Bad Access !')
	    
	      
	    
	    def  get(self , request , *args, **kwargs):
	    
		    if  self.request.user.is_authenticated and  self.request.user.username ==  self.kwargs['username']:
	    
			    return  super().get(request)
	    
		    else:
	    
			    raise Http404('Bad Access !')
	    
      
      
      
    
    class  LikeOrDislikeDeleteView(DeleteView):
    
	    model = BlogPostLike
	    
	    template_name =  "weblog/deleteLikeOrDislike_confirm.html"
	    
	      
	    
	    #hatman bayad toye delete view hedayat beshim be ye safhe ke confirm konim delete bshe ya na mese hamini ke zadim
	    
	      
	    
	    def  get_context_data(self, **kwargs):
	    
		    context =  super().get_context_data(**kwargs)
		    
		    context["username_in_url"] =  self.kwargs['username']
	    
		    return context
			    
	      
	    
	    def  get_success_url(self):
	    
		    return reverse('weblog:post', args=(self.kwargs['username'] , self.kwargs['post_id']))



