from django.http import HttpResponse, JsonResponse
from .models import Task, Person

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import TaskSerializer, PersonSerializer


# views for tasks
class TasksListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'priority', 'person__last_name', 'person__first_name')


@api_view(['GET'])
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response("Task deleted")


# views for people

class PeopleListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('last_name', 'first_name')


@api_view(['GET'])
def person_detail(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def person_create(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def person_update(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def person_delete(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    return Response("Person deleted")
