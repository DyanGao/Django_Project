'''
contains the logic that processes requests and returns responses.
It acts as an intermediary between models (data) and templates (presentation).
'''

from django.shortcuts import render
from posts.models import Post

def homepage(request):
  posts = Post.objects.all().order_by('-date')[:3]
  return render(request, 'index.html', {'posts': posts})