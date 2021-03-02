# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


def index(request):
    return HttpResponse("index page created")


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(["GET", 'POST'])
def taskList(request):
    begin = 0
    end = len(Task.objects.all())

    if 'page' in request.data:
        range = 10
        if 'range' in request.data:
            range = request.data['range']
        page = request.data['page']
        begin = (page-1)*range
        end = page*range

    if 'begin' in request.data:
        begin = request.data['begin']

    if 'end' in request.data:
        end = request.data['end']

    tasks = Task.objects.all()[begin:end]
    serializer = TaskSerializer(tasks, many=True)

    length = len(Task.objects.all())

    return Response({'begin': begin, 'end': end, 'length': length, "tasks": serializer.data})


@api_view(["GET"])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.object.get(id=pk)
    task.delete()

    return Response("Item successfully deleted!")
