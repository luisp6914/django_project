from django.shortcuts import render

'''
This is the script that handles the routes 
'''
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')
