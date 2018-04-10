from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime


# Create your views here.
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    assert isinstance(request, HttpRequest)
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)


def login(request):
    assert isinstance(request, HttpRequest)
    tparams = {
        'title': 'Login',
        'message': 'Login page.',
        'year': datetime.now().year,
    }
    return render(request, 'login.html', tparams)


def layout(request):
    return render(request, 'layout.html')
