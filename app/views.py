from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Task
from app.serializers import TaskSerializer


class TaskList(APIView):
    def get(self, request):
        serializer = TaskSerializer(Task.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """
    Retrieve,
    Update or
    Delete a task instance.
    """

    @staticmethod
    def get_task_object(pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        serializer = TaskSerializer(self.get_task_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = TaskSerializer(self.get_task_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_task_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
