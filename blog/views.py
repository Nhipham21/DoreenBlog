from typing import Any, Dict
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.http import HttpRequest
from .models import Post, Comment, Categories, SubCategories
from user.form import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/homepage.html', context)


def subcategory_detail_page(request, id):
    sub_category = SubCategories.objects.get(id=id)
    posts = Post.objects.all().filter(sub_category=sub_category.id)
    context = {
        'subcategory': sub_category,
        'posts': posts,
    }
    return render(request, 'blog/sub_category_page.html', context)


def category_detail_page(request, id):
    category_detail = Categories.objects.get(id=id)
    subcategories = SubCategories.objects.all().filter(category=category_detail.id)
    posts = Post.objects.all()

    context = {
        'category': category_detail,
        'subcategories': subcategories,
        'posts': posts,
    }
    return render(request, 'blog/category_page.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/homepage.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

    c_form = CommentForm

    # save comment when user submit
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            c_form = CommentForm(request.POST)
            if c_form.is_valid():
                post = self.get_object()
                c_form.instance.name = request.user
                c_form.instance.post = post
                c_form.save()
                messages.success(
                    request, f'You have commented in this post!')
                return redirect(reverse('post-detail', args=[str(post.pk)]))
        else:
            c_form = CommentForm()

    # get previous comments
    def get_context_data(self, **kwargs: Any):
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'c_form': self.c_form,
            'post_comments': post_comments
        })
        return context
