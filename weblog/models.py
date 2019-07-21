from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager


from django.shortcuts import render , reverse
class UserManager(BaseUserManager):
    
    def create_user(self , username , email , password = None , is_active = True , is_staff = False , is_admin = False):
        if not username:
            raise ValueError("Users Must Have a Username")
        if not email:
            raise ValueError("Users Must Have an Email")
        if not password:
            raise ValueError("Users Must Have a Password")

        user_obj = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using = self._db)
        return user_obj

    def create_staffuser(self , username , email , password = None):
        user = self.create_user(
            username,
            email,
            password = password,
            is_staff = True
        )
        return user

    def create_superuser(self , username , email , password = None):
        user = self.create_user(
            username,
            email,
            password = password,
            is_staff = True,
            is_admin = True
        )
        return user

class User(AbstractBaseUser):

    username = models.CharField(max_length=50 , primary_key = True , unique = True)
    email = models.EmailField(max_length=254 , unique = True , default = 'test@test.com')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    signup_date = models.DateTimeField(auto_now_add = True)


    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.firstname + '    ' + self.lastname   

    def get_short_name(self):
        return self.firstname

    def has_perm(self , perm , obj = None):
        return True

    def has_module_perms(self , app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
        
    @property
    def is_active(self):
        return self.active 

# Create your models here.
class Skill(models.Model):

    skillName = models.CharField(max_length=100 , primary_key = True)

    def __str__(self):
        return self.skillName

    def __unicode__(self):
        return


class UserDetail(models.Model):

    user = models.OneToOneField(User , on_delete = models.CASCADE ,null=True)

    # username = models.CharField(max_length=50 , primary_key=True)
    # password = models.CharField(max_length=100)
    # firstname = models.CharField(max_length = 100)
    # lastname = models.CharField(max_length = 100)
    # email = models.EmailField(max_length=254 , unique = True)
    # admin = models.BooleanField(default = 0)
    # signup_date = models.DateTimeField(auto_now_add=True)
    # account_status = models.CharField(default = 'Active' , max_length = 250)



    github_link = models.URLField(blank=True, null=True , max_length=200)
    facebook_link = models.URLField(blank=True, null=True , max_length=200)
    Linkedin_link = models.URLField(blank=True, null=True , max_length=200)
    Instagram_link = models.URLField(blank=True, null=True , max_length=200)
    Telegram_link = models.URLField(blank=True, null=True , max_length=200)
    personal_website = models.URLField(blank=True, null=True , max_length=200)
    aboutme = models.CharField(blank=True, null=True , max_length=50)
    bio = models.TextField(blank=True, null=True)
    primary_skill = models.ForeignKey(Skill, default = 'Nothing' ,related_name ='user_who_have_this_as_primary' ,on_delete=models.CASCADE)
    secondary_skill = models.ForeignKey(Skill, default = 'Nothing' ,related_name = 'user_who_have_this_as_secondary' ,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'weblog/profile_pics' , blank=True)
    is_private = models.BooleanField(default = False)
    rank = models.CharField(blank=True, null=True , max_length=200)
    phone = models.CharField(blank=True, null=True,max_length=15)
    profession = models.CharField(blank=True, null=True , max_length=50)


    def __str__(self):
        return str(self.user) + ' / Primary : ' + str(self.primary_skill) + ' / Secondary : ' + str(self.secondary_skill)

    def __unicode__(self):
        return



class BlogPost(models.Model):

    #id = pk
    title = models.CharField(max_length = 100 , null = False , unique = True)
    body = models.TextField(null = False)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    post_pic = models.ImageField(upload_to='weblog/post_pics', max_length=None , blank=True, null=True)
    def __str__(self):
        return 'USER : ' + str(self.username) + ' / ' + str(self.pk) + ' - Title :  "' + self.title + '" / Likes : ' + str(self.blogpostlike_set.count())
    def __unicode__(self):
        return


    def get_absolute_url(self):
        return reverse("weblog:post", kwargs={"pk": self.pk , 'username' : self.username})
    

class Comment(models.Model):

    #id = pk
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=250)
    blogPost_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.comment_text

    def __unicode__(self):
        return



class BlogPostLike(models.Model):

    #id = pk
    likes = models.BooleanField(default = 0)
    blogPost_id = models.ForeignKey(BlogPost , on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('blogPost_id', 'username',)
    def __str__(self):
        return str(self.username) + ' Likes --> ' + str(self.blogPost_id)

    def __unicode__(self):
        return

class CommentLike(models.Model):

    #id = pk
    likes = models.BooleanField(default = 0)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('comment_id', 'username',)
    def __str__(self):
        return str(self.username) + ' Likes --> ' + str(self.comment_id)
    def __unicode__(self):
        return
