from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from .models import Task, Person

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import TaskSerializer, PersonSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins


# views for tasks
class TasksListView(mixins.PermissionRequiredMixin, generics.ListAPIView):
    permission_required = 'tasks.view_task'
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'priority', 'person__last_name', 'person__first_name')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TasksListView, self).dispatch(request, *args, **kwargs)


@api_view(['GET'])
@login_required
@permission_required('tasks.view_task')
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@login_required
@permission_required('tasks.add_task')
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
@login_required
@permission_required('tasks.change_task')
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
@login_required
@permission_required('tasks.delete_task')
def task_delete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response("Task deleted")


# views for people
class PeopleListView(mixins.PermissionRequiredMixin, generics.ListAPIView):
    permission_required = 'tasks.view_person'
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('last_name', 'first_name')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PeopleListView, self).dispatch(request, *args, **kwargs)


@api_view(['GET'])
@login_required
@permission_required('tasks.view_person')
def person_detail(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@login_required
@permission_required('tasks.add_person')
def person_create(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
@login_required
def person_update(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
@login_required
@permission_required('tasks.delete_person')
def person_delete(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    return Response("Person deleted")
