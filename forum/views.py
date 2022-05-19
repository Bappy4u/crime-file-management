from django.shortcuts import render
from .models import Post



def forumView(request):
    posts = Post.objects.select_related('category').all()
    context = {
        'posts': posts
    }
    return render(request, 'forum.html', context)
