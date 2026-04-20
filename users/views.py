from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import registerationForm
from django.contrib.auth.decorators import login_required
from blog.models import Post

def register(request):
    if request.method == 'POST':
        form = registerationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request, message= f'Your account has been created! you are now able to login')
            return redirect('login')
    else:
        form = registerationForm()

    return render(request, template_name='users/register.html',context={"form":form})

@login_required
def profile(request):
    user_posts = Post.objects.filter(author_id = request.user.id)
    return render(request=request, template_name='users/profile.html',context={"user_posts": user_posts})
