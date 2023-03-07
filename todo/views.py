# from django.shortcuts import render
from rest_framework import viewsets
from todo.models import User, Task
from todo.serializer import UserSerializer, TaskSerializer


# 4 - Quarta Etapa (proximo passo em urls.py)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
