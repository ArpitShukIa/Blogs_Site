from django.shortcuts import render


def home(request):
    posts = []
    return render(request, 'blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')
