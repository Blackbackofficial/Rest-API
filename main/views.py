from django.http import JsonResponse, QueryDict
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.parsers import JSONParser
from .forms import PersonForm
from .models import Person
from .serializers import PersonSerializer
import json


#  Rest API CRUD for Person
# @api_view(['GET'])
# def get_persons(request, pk):
#     if request.method == 'GET':
#         try:
#             persons = Person.objects.get(pk=pk)
#             persons_serializer = PersonSerializer(persons)
#             return JsonResponse(persons_serializer.data)
#         except Person.DoesNotExist:
#             return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def all_persons(request):
#     if request.method == 'GET':
#         persons = Person.objects.all()
#         serializer = PersonSerializer(persons, many=True)
#         return JsonResponse({"persons": serializer.data}, safe=False)


@api_view(['PATCH', 'DELETE', 'GET'])
def up_del_person(request, pk):
    try:
        pk = pk + 1
        person_safe = Person.objects.get(id=pk)
    except Person.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist or No Content'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            persons = Person.objects.get(pk=pk)
            persons_serializer = PersonSerializer(persons)
            i = int(persons_serializer.data['id']) - 1
            res = persons_serializer.data
            res['id'] = i
            return JsonResponse(res, status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        person = JSONParser().parse(request)
        serializer = PersonSerializer(instance=person_safe, data=person, partial=True)
        if serializer.is_valid(raise_exception=True):
            person_save = serializer.save()
            persons = Person.objects.get(pk=pk)
            persons_serializer = PersonSerializer(persons)
            i = int(persons_serializer.data['id']) - 1
            res = persons_serializer.data
            res['id'] = i
            return JsonResponse(res, status=status.HTTP_200_OK, safe=False)

    if request.method == 'DELETE':
        person_safe.delete()
        return JsonResponse('', status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def creat_persons(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        # sum = Person.objects.count()
        serializer = PersonSerializer(persons, many=True)
        for i in serializer.data:
            i = int(i['id']) - 1
            serializer.data[i]['id'] = i

        return JsonResponse({"persons": serializer.data}, safe=False)
    if request.method == 'POST':
        persons = JSONParser().parse(request)
        last_id = Person.objects.count()
        persons['id'] = last_id
        person_serializer = PersonSerializer(data=persons)
        if person_serializer.is_valid():
            persons_saved = person_serializer.save()
            response = JsonResponse('', status=status.HTTP_201_CREATED, safe=False)
            response['Location'] = (
                'Location', 'https://rsoi-person-service.herokuapp.com/person/{}'.format(last_id)
            )
            return response
        return JsonResponse(person_serializer.errors, status=status.HTTP_404_NOT_FOUND, safe=False)


# SiteView
def index(request):
    persons = Person.objects.order_by('-name')  # А так же можно отсортировать полюбому другому полю, можно указать
    return render(request, 'main/index.html',
                  {
                      'title': 'Главная страница',
                      'name': persons
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
