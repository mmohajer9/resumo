from weblog.models import BlogPostLike
from django import template
from django.conf import settings

register = template.Library()

@register.filter
def truelikesCount(blogpostlike_set, category = 1):
    return blogpostlike_set.filter(likes=category).count()

@register.filter
def truedislikesCount(blogpostlike_set, category = 0):
    return blogpostlike_set.filter(likes=category).count()