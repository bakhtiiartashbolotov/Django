from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data = "Hello"
    return render(request, 'home.html', {'data': data})

def blog(request):
    blog_posts = [
        {'title': 'Blog Post 1', 'content': 'Content for Blog Post 1'},
        {'title': 'Blog Post 2', 'content': 'Content for Blog Post 2'},
        {'title': 'Blog Post 3', 'content': 'Content for Blog Post 3'},
    ]
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def products(request):
    products = [
        {'name': 'Product 1', 'price': 19.99, 'description': 'Description for Product 1'},
        {'name': 'Product 2', 'price': 29.99, 'description': 'Description for Product 2'},
        {'name': 'Product 3', 'price': 39.99, 'description': 'Description for Product 3'},
    ]
    return render(request, 'products.html', {'products': products})