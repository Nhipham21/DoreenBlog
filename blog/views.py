from django.shortcuts import render
from django.http import HttpRequest
from .models import Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/homepage.html', context)
