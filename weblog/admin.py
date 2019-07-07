from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserDetail)

admin.site.register(Skill)

admin.site.register(BlogPost)

admin.site.register(BlogPostLike)

admin.site.register(CommentLike)

admin.site.register(Comment)