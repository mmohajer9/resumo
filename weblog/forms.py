from django import forms
from django.core import validators
from .models import *
from captcha.fields import CaptchaField 

# class signupForm(forms.Form):

#     i = 1
#     skill_choice = []
#     skill_set = Skill.objects.all()
#     for skill in skill_set:
#         skill_choice.append(  (str(i) , str(skill))  )
#         i += 1
#     print(skill_choice)

#     username = forms.CharField(max_length=50)
#     password = forms.CharField(max_length=100, widget = forms.PasswordInput)
#     firstname = forms.CharField(max_length = 100)
#     lastname = forms.CharField(max_length = 100)
#     email = forms.EmailField(max_length=254 , required=False)
#     verifyEmail = forms.EmailField(label='Enter Your Email Again: ')
#     github_link = forms.URLField(max_length=200 , required=False)
#     facebook_link = forms.URLField(max_length=200 , required=False)
#     Linkedin_link = forms.URLField(max_length=200 , required=False)
#     Instagram_link = forms.URLField(max_length=200 , required=False)
#     Telegram_link = forms.URLField(max_length=200 , required=False)
#     Telegram_ID = forms.CharField(max_length=200 , required=False)
#     primary_skill = forms.CharField(required=False , widget = forms.Select(choices = skill_choice))
#     secondary_skill = forms.CharField(required=False , widget = forms.Select(choices = skill_choice))
#     aboutme = forms.CharField(required = False)
#     botcatcher = forms.CharField(required=False , widget = forms.HiddenInput , validators=[validators.MaxLengthValidator(0)])


    # def clean_botcatcher(self):
    #     print('form method of clean_botcatcher called')
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('BOT Caputured!')

    #     return botcatcher

    # def clean_verifyEmail(self):
    #     print('form method of verifyMail called')
    #     email = self.cleaned_data['email']
    #     verifyEmail = self.cleaned_data['verifyEmail']

    #     if email != verifyEmail:
    #         raise forms.ValidationError('Emails Are not Match Together')
    #     return verifyEmail

class signupForm(forms.ModelForm):
    verifyEmail = forms.EmailField(label='Verify Your Email: ')
    botcatcher = forms.CharField(required=False , widget = forms.HiddenInput , validators=[validators.MaxLengthValidator(0)])
    captcha = CaptchaField()
    class Meta:
        model = UserDetail
        fields = ('username' , 'password' , 'firstname' , 'lastname' , 'email' , 'primary_skill' , 'secondary_skill' ,)
        widgets = {
            'password' : forms.PasswordInput(),
        }
    
    def clean_botcatcher(self):
        print('form method of clean_botcatcher called')
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('BOT Caputured!')

        return botcatcher

    def clean_verifyEmail(self):
        print('form method of verifyMail called')
        email = self.cleaned_data['email']
        verifyEmail = self.cleaned_data['verifyEmail']

        if email != verifyEmail:
            raise forms.ValidationError('Emails Are not Match Together')
        return verifyEmail

class additional_info_Form(forms.ModelForm):
    github_link = forms.URLField(required=False)
    facebook_link = forms.URLField(required=False)
    Linkedin_link = forms.URLField(required=False)
    Instagram_link = forms.URLField(required=False)
    Telegram_link = forms.URLField(required=False)
    Telegram_ID = forms.CharField(required=False)
    class Meta:
        model = UserDetail
        fields = ('github_link' , 'facebook_link' , 'Linkedin_link' , 'Instagram_link' , 'Instagram_link' , 'Telegram_link' , 'aboutme' ,)
        