from django.shortcuts import render, redirect

def astro(request):
    return render(request, 'astro.html')


def kamni(request):
    return render(request, 'kamni.html')


def main(request):
    return render(request, 'main.html')


def progect(request):
    return render(request, 'progect.html')


def samocv(request):
    return render(request, 'samocv.html')

def algorithm(request):
    return render(request, 'algorithm.html')