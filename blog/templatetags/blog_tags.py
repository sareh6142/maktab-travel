from django import template
from blog.models import Post,Category
from blog.models import Comment
register = template.Library()


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(args:2):
    posts = Post.objects.filter(status=1).order_by('published_date')[:args]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status = 1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]= posts.filter(category = name).count()
    return{'categories':cat_dict}

@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.get(pk = pid)
    return Comment.objects.filter(post=post.id,approved = True).count()
