from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(req):
    posts = Post.objects.order_by('-pub_date')
    return render(req, 'posts/home.html', {'posts':posts})

def post_details(req, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(req, 'posts/posts_detail.html', {'post':post})