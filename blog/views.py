from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post


posts = Post.objects.all()

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request=request,template_name='blog/home.html',context=context)

def about(request):
    return  render(request=request,template_name='blog/about.html',context={'title': 'About'})