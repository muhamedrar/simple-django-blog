from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'titel':'this is post one',
        'author': 'john doe',
        'date': '12 Mar 2021',
        'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse quis iaculis leo. Integer ultricies interdum risus at faucibus. Nunc quis pharetra elit. Duis sit amet turpis vitae leo semper vulputate. Praesent molestie in urna suscipit volutpat. Duis vitae sodales dolor. Nunc mi nibh, laoreet eu euismod non, scelerisque sed ex. Vivamus non mi feugiat libero vulputate dapibus sed in mauris. Curabitur nisl tellus, egestas sed tempus vitae, congue et nisi. Proin consequat metus quis purus blandit tincidunt. Aenean commodo sit amet erat a facilisis. Nam ac hendrerit enim. Duis varius dolor nec dolor rutrum commodo. Aliquam velit nulla, imperdiet ac ante vitae, faucibus ullamcorper sem. Nunc suscipit laoreet nisl, ac rhoncus magna dignissim rhoncus. Curabitur dignissim felis lacus, vel tempor nulla condimentum ac.'
    },
    {
        'titel':'this is post two',
        'author': 'another john doe',
        'date': '19 Mar 2021',
        'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse quis iaculis leo. Integer ultricies interdum risus at faucibus. Nunc quis pharetra elit. Duis sit amet turpis vitae leo semper vulputate. Praesent molestie in urna suscipit volutpat. Duis vitae sodales dolor. Nunc mi nibh, laoreet eu euismod non, scelerisque sed ex. Vivamus non mi feugiat libero vulputate dapibus sed in mauris. Curabitur nisl tellus, egestas sed tempus vitae, congue et nisi. Proin consequat metus quis purus blandit tincidunt. Aenean commodo sit amet erat a facilisis. Nam ac hendrerit enim. Duis varius dolor nec dolor rutrum commodo. Aliquam velit nulla, imperdiet ac ante vitae, faucibus ullamcorper sem. Nunc suscipit laoreet nisl, ac rhoncus magna dignissim rhoncus. Curabitur dignissim felis lacus, vel tempor nulla condimentum ac.'
    },
    
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request=request,template_name='blog/home.html',context=context)

def about(request):
    return  render(request=request,template_name='blog/about.html',context={'title': 'About'})