from ipware import get_client_ip
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import TodoList
from todo.serializers import TodoListSerializer


@api_view(['GET', 'POST'])
def todo_list(request):
    """Function to get all object and create new model object"""
    if request.method == 'GET':
        todo_list = TodoList.objects.all()
        todo_list_serializer = TodoListSerializer(todo_list, many = True)
        return Response(todo_list_serializer.data)

    elif request.method == 'POST':
        todo_list_serializer = TodoListSerializer(data = request.data)
        author_ip, is_routable = get_client_ip(request)
        if todo_list_serializer.is_valid():
            todo_list_serializer.save(author_ip = author_ip)
            return Response({'task_id': todo_list_serializer.data['id']})
        return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def todo_detail(request, pk):
    """Function to get partial update and delete if exist specified
        object if not return 404 status """
    try:
        todo = TodoList.objects.get(pk = pk)
    except TodoList.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        todo_serializer = TodoListSerializer(todo)
        return Response(todo_serializer.data)

    elif request.method == 'PATCH':
        todo_serializer = TodoListSerializer(todo, data = request.data, partial = True)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
