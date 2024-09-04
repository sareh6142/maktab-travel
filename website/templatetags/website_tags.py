from django import template
from blog.models import Post,Category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('website/six_latest_posts.html')
def six_latest_posts():
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now() ).order_by('-published_date')[0:6]
    return {'posts':posts}