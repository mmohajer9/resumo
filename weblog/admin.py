from django.contrib import admin
from .models import *
from django import forms

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


#Customizing Admin ModelForm
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
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

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username' ,'email', 'password', 'active', 'staff' , 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'active' , 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('firstname','lastname')}),
        ('Permissions', {'fields': ('admin','staff' , 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()




# Register your models here.
admin.site.unregister(Group)

admin.site.register(User , UserAdmin)

admin.site.register(UserDetail)

admin.site.register(Skill)

admin.site.register(BlogPost)

admin.site.register(BlogPostLike)

admin.site.register(CommentLike)

admin.site.register(Comment)