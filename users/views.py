from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import registerationForm

def register(request):
    if request.method == 'POST':
        form = registerationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request, message= f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = registerationForm()

    return render(request, template_name='users/register.html',context={"form":form})
