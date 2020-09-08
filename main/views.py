from django.shortcuts import render, redirect

from . import forms
from .forms import PersonForm
from .models import Person


def index(request):
    # persons = Person.objects.all()  # Можно вывести все
    persons = Person.objects.order_by('-person')  # А так же можно отсортировать полюбому другому полю, можно указать
    # "-" тогда сортировка в обратном порядке
    # persons = Person.objects.order_by('-person')[:3]  # Выбрать лишь 3 первых записи
    return render(request, 'main/index.html',
                  {
                      'title': 'Главная страница',
                      'persons': persons
                  })


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Ошибка'

    form = PersonForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
