from django.shortcuts import render, redirect
from .forms import ReplyForm

def create_reply(request):
    error = ''
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('main')
        else:
            print(form.errors)
            error = 'Форма была отправлена неверной'
    form = ReplyForm()

    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'create_reply.html', data)