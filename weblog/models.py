from django.db import models

# Create your models here.
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

    def __str__(self):
        return username , password , firstname , lastname

    def __unicode__(self):
        return 



class BlogPost(models.Model):
    
    #id = pk
    
    def __str__(self):
        return 

    def __unicode__(self):
        return 




class Like(models.Model):
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 




class Comment(models.Model):
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 


