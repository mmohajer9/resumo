from django.db import models
from django.db.models.functions import Concat
# Create your models here.
class Skill(models.Model):

    skillName = models.CharField(max_length=100 , primary_key = True)

    def __str__(self):
        return self.skillName

    def __unicode__(self):
        return


class UserDetail(models.Model):

    username = models.CharField(max_length=50 , primary_key=True)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField(max_length=254 , unique = True)
    github_link = models.URLField(null = True , default= 'http://localhost' , max_length=200)
    facebook_link = models.URLField(null = True, default= 'http://localhost' , max_length=200)
    Linkedin_link = models.URLField(null = True, default= 'http://localhost' , max_length=200)
    Instagram_link = models.URLField(null = True, default= 'http://localhost' , max_length=200)
    Telegram_link = models.URLField(null = True, default= 'http://localhost' , max_length=200)
    Telegram_ID = models.CharField(null = True, default= 'http://localhost' , max_length=200)
    aboutme = models.TextField(default = 'No Informations!')
    primary_skill = models.ForeignKey(Skill, default = 'Dumb' ,related_name ='user_who_have_this_as_primary' ,on_delete=models.CASCADE)
    secondary_skill = models.ForeignKey(Skill, default = 'Dumb' ,related_name = 'user_who_have_this_as_secondary' ,on_delete=models.CASCADE)
    admin = models.BooleanField(default = 0)
    signup_date = models.DateTimeField(auto_now=True)
    account_status = models.CharField(default = 'Active' , max_length = 250)


    def __str__(self):
        return self.username

    def __unicode__(self):
        return



class BlogPost(models.Model):

    #id = pk
    title = models.CharField(max_length = 100 , null = False)
    body = models.TextField(null = False)
    username = models.ForeignKey(UserDetail,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return 'USER : ' + str(self.username) + ' / ' + str(self.pk) + ' - Title :  "' + self.title + '" / Likes : ' + str(self.blogpostlike_set.count())
    def __unicode__(self):
        return


class Comment(models.Model):

    #id = pk
    username = models.ForeignKey(UserDetail,default = 'Unknown',on_delete=models.CASCADE)
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
    username = models.ForeignKey(UserDetail,default =  'Unknown' ,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username) + ' Likes --> ' + str(self.blogPost_id)

    def __unicode__(self):
        return

class CommentLike(models.Model):

    #id = pk
    likes = models.BooleanField(default = 0)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    username = models.ForeignKey(UserDetail,default = 'Unknown',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username) + ' Likes --> ' + str(self.comment_id)
    def __unicode__(self):
        return
