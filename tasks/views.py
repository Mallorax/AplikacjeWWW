from django.http import HttpResponse, JsonResponse
from .models import Task, Person

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, PersonSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': 'tasks-list',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)


# views for tasks
@api_view(['GET'])
def tasks_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


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
@api_view(['GET'])
def person_list(request):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)


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
