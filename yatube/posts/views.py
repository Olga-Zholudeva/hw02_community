from django.shortcuts import render, get_object_or_404
from .models import Post, Group

LIMIT_POSTS = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:LIMIT_POSTS]
    return render(request, 'posts/index.html', {'posts': posts, })


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = (
        Post.objects.filter(group=group).order_by('-pub_date')[:LIMIT_POSTS]
    )
    return render(
        request, 'posts/group_list.html', {'group': group, 'posts': posts, }
    )
