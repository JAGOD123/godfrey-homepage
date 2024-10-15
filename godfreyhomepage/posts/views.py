from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(requet):
    posts = Post.objects.all().order_by('-date')
    return render(requet, 'posts/posts_list.html', {'posts': posts})
