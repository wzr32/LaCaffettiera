from django.shortcuts import render
from .models import *

# Create your views here.

def services(request):
    services = Services.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services/services.html', context)
