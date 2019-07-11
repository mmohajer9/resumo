from django import forms
from django.core import validators
from .models import *
class signupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length = 100)
    lastname = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length=254)
    github_link = forms.URLField(max_length=200 , initial='http://localhost')
    facebook_link = forms.URLField(max_length=200 , initial='http://localhost')
    Linkedin_link = forms.URLField(max_length=200 , initial='http://localhost')
    Instagram_link = forms.URLField(max_length=200 , initial='http://localhost')
    Telegram_link = forms.URLField(max_length=200 , initial='http://localhost')
    Telegram_ID = forms.CharField(max_length=200 , initial='http://localhost')
    primary_skill = forms.CharField()
    secondary_skill = forms.CharField()
    aboutme = forms.CharField(required = False)
    botcatcher = forms.CharField(required=False , widget = forms.HiddenInput , validators=[validators.MaxLengthValidator(0)])


    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('BOT Caputured!')

        return botcatcher
