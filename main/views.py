from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .forms import PersonForm
from .models import Person
from .serializers import PersonSerializer


#  Rest API CRUD
@api_view(['GET'])
def get_persons(request, pk):
    if request.method == 'GET':
        try:
            persons = Person.objects.get(pk=pk)
            persons_serializer = PersonSerializer(persons)
            return JsonResponse(persons_serializer.data)
        except Person.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_persons(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return JsonResponse({"persons": serializer.data})


@api_view(['PATCH', 'DELETE'])
def up_del_person(request, pk):
    try:
        person_safe = Person.objects.get(id=pk)
    except Person.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist or No Content'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        person = JSONParser().parse(request)
        serializer = PersonSerializer(instance=person_safe, data=person, partial=True)
        if serializer.is_valid(raise_exception=True):
            person_save = serializer.save()
            return JsonResponse({
                "success": "Persons '{}' updated successfully".format(person_save.person)
            })

    if request.method == 'DELETE':
        person_safe.delete()
        return JsonResponse({
            "message": "Person with id `{}` has been deleted.".format(pk)
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def creat_persons(request):
    if request.method == 'POST':
        persons = JSONParser().parse(request)
        last_id = Person.objects.count() + 1
        persons['id'] = last_id
        serializer = PersonSerializer(data=persons)
        if serializer.is_valid(raise_exception=True):
            persons_saved = serializer.save()
            response = JsonResponse(persons_saved.id, status=status.HTTP_201_CREATED, safe=False)
            response.headers['Location'] = (
                'Location', 'https://rsoi-person-service.herokuapp.com/person/{}'.format(persons_saved.pk)
            )
            return response
        return JsonResponse(persons_saved.errors, status=status.HTTP_404_NOT_FOUND, safe=False)


# SiteView
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
