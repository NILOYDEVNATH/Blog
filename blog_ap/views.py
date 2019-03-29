from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'blog_ap/home.html')

def about(request):
    return render(request, 'blog_ap/about.html')

def post(request):
    return render(request, 'blog_ap/post.html')

def contact(request):
    return render(request, 'blog_ap/contact.html')
