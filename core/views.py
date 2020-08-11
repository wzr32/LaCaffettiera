from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def history(request):
    return render(request, 'core/history.html')

def store(request):
    return render(request, 'core/store.html')

def contact(request):
    return render(request, 'core/contact.html')

def blog(request):
    return render(request, 'core/blog.html')

def sample(request):
    return render(request, 'core/sample.html')