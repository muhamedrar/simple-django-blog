from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import registerationForm, userUpdateForm, userUpdateImage
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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

    if request.method == 'POST':
        u_form  = userUpdateForm(request.POST,instance=request.user)
        p_form = userUpdateImage(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request=request, message= f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = userUpdateImage(instance=request.user.profile)


    context = {
        'user_posts': user_posts,
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request=request, template_name='users/profile.html',context=context)




