from django.shortcuts import render
from django.http import HttpResponse

'''
This is the script that handles the routes 
'''
# Create your views here.
def home(request):
    return HttpResponse(" <h1> Blog Home </h1> ")

def about(request):
    return HttpResponse(" <h1> Blog About </h1> ")
