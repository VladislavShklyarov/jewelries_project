import math

from django.shortcuts import render, redirect
from .models import Algorithm
from .forms import AlgorithmForm


def algorithm(request):
    if request.method == 'POST':
        form = AlgorithmForm(request.POST)
        if form.is_valid():
            D = form.cleaned_data['D']
            A = form.cleaned_data['A']

            result = (D >= math.sqrt(2) * A)
            if result == True:
                result = "Можно выпилить"
            else:
                result = 'Нельзя выпилить'

            Algorithm.objects.create(D=D, A=A, result=result)
            return redirect('result')

    else:
        form = AlgorithmForm()

    context = {'form': form}
    return render(request, 'algorithm.html', context)


def result(request):
    results = Algorithm.objects.order_by('result')
    return render(request, 'results.html', {'results': results})
