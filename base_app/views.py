from django.shortcuts import render

def home (request):
    return render(request, 'pages/home.html')

def about (request):
    return render(request, 'pages/about.html')

def contact (request):
    return render(request, 'pages/contact.html')

def login (request):
    return render(request, 'pages/login.html')

def register (request):
    return render(request, 'pages/register.html')