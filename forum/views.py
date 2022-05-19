from django.http import Http404
from django.shortcuts import render
from .models import Post



def forumView(request):
    posts = Post.objects.select_related('category').all()
    context = {
        'posts': posts
    }
    return render(request, 'forum.html', context)


def postView(request, id):
    try:
        post = Post.objects.select_related('category').get(pk=id)
    except Post.DoesNotExist:
        raise Http404("File does not exist")
        
    context = {
        'post': post
    }
    return render(request, 'post.html', context)
