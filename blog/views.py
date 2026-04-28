from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import ListView

posts = Post.objects.all()


# def home(request):
#     context = {
#         'posts': posts
#     }
#     return render(request=request,template_name='blog/home.html',context=context)


class PostViews(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = '-data_posted'

def about(request):
    return  render(request=request,template_name='blog/about.html',context={'title': 'About'})