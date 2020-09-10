from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import PersonForm
from .models import Person
from .serializers import PersonSerializer


# class PersonView(APIView):
#
#     def get(self, request, pk):
#         if request.method == 'GET':
#             try:
#                 persons = Person.objects.get(pk=pk)
#                 persons_serializer = PersonSerializer(persons)
#                 return Response(persons_serializer.data)
#             except Exception as ex:
#                 print(ex)
#
#     # def get(self, request):
#     #     if request.method == 'GET':
#     #         try:
#     #             persons = Person.objects.all()
#     #
#     #             serializer = PersonSerializer(persons, many=True)
#     #             return Response({"persons": serializer.data})
#     #         except Exception as ex:
#     #             print(ex)
#
#     def post(self, request):
#         if request.method == 'POST':
#             try:
#                 persons = JSONParser().parse(request)
#                 persons_saved = ""
#                 serializer = PersonSerializer(data=persons)
#                 if serializer.is_valid(raise_exception=True):
#                     persons_saved = serializer.save()
#                     # HttpResponse.__setitem__("Location", "efwdweewdwed")
#                     resp = JsonResponse(persons_saved.id, status=status.HTTP_201_CREATED, safe=False)
#                     print((resp.__class__, resp))
#                     Resp = resp.__setitem__("Location", "https://rsoi-person-service.herokuapp.com/person/{personId}")
#                     print(resp.__class__, resp)
#                     return JsonResponse(Resp, safe=False)
#                 return JsonResponse(persons_saved.errors, status=status.HTTP_404_NOT_FOUND, safe=False)
#             except Person.DoesNotExist:
#                 return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     def patch(self, request, pk):
#         if request.method == 'PATCH':
#             person_save = get_object_or_404(Person.objects.all(), id=pk)
#             person = JSONParser().parse(request)
#             serializer = PersonSerializer(instance=person_save, data=person, partial=True)
#             if serializer.is_valid(raise_exception=True):
#                 person_save = serializer.save()
#             return JsonResponse({
#                 "success": "Persons '{}' updated successfully".format(person_save.person)
#             })


@api_view(['GET'])
def get_persons(request, pk):
    if request.method == 'GET':
        try:
            persons = Person.objects.get(pk=pk)
            persons_serializer = PersonSerializer(persons)
            return JsonResponse(persons_serializer.data)
        except Exception as ex:
            print(ex)


@api_view(['GET'])
def all_persons(request):
    if request.method == 'GET':
        try:
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
            return JsonResponse({"persons": serializer.data})
        except Exception as ex:
            print(ex)


@api_view(['PATCH', 'DELETE'])
def up_del_person(request, pk):
    if request.method == 'PATCH':
        person_save = get_object_or_404(Person.objects.all(), id=pk)
        person = JSONParser().parse(request)
        serializer = PersonSerializer(instance=person_save, data=person, partial=True)
        if serializer.is_valid(raise_exception=True):
            person_save = serializer.save()
        return JsonResponse({"success": "Persons '{}' updated successfully".format(person_save.person)})

    if request.method == 'DELETE':
        person = get_object_or_404(Person.objects.all(), pk=pk)
        person.delete()
        return JsonResponse({"message": "Person with id `{}` has been deleted.".format(pk)},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def creat_persons(request):
    if request.method == 'POST':
        persons = JSONParser().parse(request)
        persons_saved = ""
        serializer = PersonSerializer(data=persons)
        if serializer.is_valid(raise_exception=True):
            persons_saved = serializer.save()
            return JsonResponse(persons_saved.person, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(persons_saved.errors, status=status.HTTP_404_NOT_FOUND, safe=False)  # Добавить ошибку 404


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
