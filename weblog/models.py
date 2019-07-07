from django.db import models

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
    email = models.EmailField(max_length=254)
    github_link = models.URLField(null = True , max_length=200)
    facebook_link = models.URLField(null = True , max_length=200)
    Linkedin_link = models.URLField(null = True , max_length=200)
    Instagram_link = models.URLField(null = True , max_length=200)
    Telegram_link = models.URLField(null = True , max_length=200)
    Telegram_ID = models.CharField(null = True , max_length=200)
    aboutme = models.TextField(default = 'No Informations!')
    primary_skill = models.ForeignKey(Skill, default = 'Dumb' ,related_name ='user_who_have_this_as_primary' ,on_delete=models.CASCADE)
    secondary_skill = models.ForeignKey(Skill, default = 'Dumb' ,related_name = 'user_who_have_this_as_secondary' ,on_delete=models.CASCADE)
    admin = models.BooleanField(default = 0)


    def __str__(self):
        return self.username

    def __unicode__(self):
        return 



class BlogPost(models.Model):
    
    #id = pk
    title = models.CharField(max_length = 100 , null = False)
    body = models.TextField(null = False)
    username = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def __unicode__(self):
        return 


class Comment(models.Model):
    
    #id = pk
    comment_text = models.CharField(max_length=250)
    blogPost_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_text

    def __unicode__(self):
        return 



class Like(models.Model):
    
    #id = pk
    likes = models.IntegerField(default = 0)
    username = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    blogPost_id = models.ForeignKey(BlogPost , on_delete=models.CASCADE)
    def __str__(self):
        return self.likes

    def __unicode__(self):
        return 





