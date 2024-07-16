from django.shortcuts import render
from posts.models import Post

def homepage(request):
  posts = Post.objects.all().order_by('-date')[:3]
  return render(request, 'index.html', {'posts': posts})