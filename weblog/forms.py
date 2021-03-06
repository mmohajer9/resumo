from django import forms
from django.core import validators
from .models import *
from captcha.fields import CaptchaField 

'''Training For Creating Forms from forms.Form() V1'''

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




'''Creating Forms from ModelForm and Submiting Data to Database V2'''

class signupForm(forms.ModelForm):
    
    verifyEmail = forms.EmailField(label='Verify Your Email')
    botcatcher = forms.CharField(required=False , widget = forms.HiddenInput , validators=[validators.MaxLengthValidator(0)])
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('username' , 'password' , 'firstname' , 'lastname' , 'email' ,)
        widgets = {
            'password' : forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'username' : forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'firstname' : forms.TextInput(attrs={'placeholder': 'e.g. Mohammad'}),
            'lastname' : forms.TextInput(attrs={'placeholder': 'e.g. Ahmadi'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'test@test.com'}),
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



        #save bayad override bshe! chon hash nadare save ghabli
        
    def save(self, commit = True):
        user = super().save(commit = False) # Call the real save() method
        user.set_password(self.cleaned_data['password'])
        if(commit):
            user.save()
        return user


class additional_info_Form(forms.ModelForm):
    github_link = forms.URLField(required=False)
    facebook_link = forms.URLField(required=False)
    Linkedin_link = forms.URLField(required=False)
    Instagram_link = forms.URLField(required=False)
    Telegram_link = forms.URLField(required=False)
    personal_website = forms.URLField(required=False)
    profile_pic = forms.ImageField(required = False)
    class Meta:
        model = UserDetail
        fields = ('primary_skill' , 'secondary_skill' , 'github_link' , 'facebook_link' , 'Linkedin_link' , 'Instagram_link' , 'Instagram_link' , 'Telegram_link' , 'personal_website' , 'aboutme' , 'profile_pic' , 'profession' , 'phone')
        