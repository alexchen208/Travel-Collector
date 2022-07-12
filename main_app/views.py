from django.shortcuts import render
from django.views.generic import ListView
from . models import Travel



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def travels_index(request):
    travels = Travel.objects.all()
    return render(request, 'travels/index.html', { 'travels': travels })

def travels_detail(request, travel_id):
    travel = Travel.objects.get(id=travel_id)
    return render(request, 'travels/detail.html', { 'travel': travel })
