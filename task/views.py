from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from task.serializers import TaskSerializer
import requests

# CRUD APIs
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Third-party API Integration
@api_view(['GET'])
def random_joke(request):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    return Response(response.json())


# Simple Report (Data Visualization)
@api_view(['GET'])
def task_report(request):
    total = Task.objects.count()
    completed = Task.objects.filter(completed=True).count()
    pending = total - completed

    return Response({
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending
    })
