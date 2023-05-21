from django.shortcuts import render
from .models import Gemstone

def shop(request):
    gemstones = Gemstone.objects.all()
    return render(request, 'shop.html', {'gemstones': gemstones})