from django.shortcuts import render
from .models import Post


def main_page(request):
    return render(request, 'base.html')


def about(request):
    with open('posts/about.txt', 'r') as file:
        data = file.read()
    return render(request, 'about.html', {'data': data})


def contacts(request):
    with open('posts/contacts.txt', 'r') as file:
        contact = file.read()
    return render(request, 'contacts.html', {'contact' : contact})


def gallery(request):
    post = Post.objects.all()
    return render(request, 'gallery.html', {'post':post})
