from django.shortcuts import render

'''
This is the script that handles the routes 
'''
# Create your views here.
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'This is the content of the first blog post',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'This is the content of the second blog post',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
