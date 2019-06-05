from ipware import get_client_ip
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from todo.models import TodoList
from todo.serializers import TodoListSerializer


class TodoListView(generics.ListCreateAPIView):
    """Class to get all and create new object"""
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    name = 'todolist'

    def post(self, request, *args, **kwargs):
        author_ip, is_routable = get_client_ip(request)
        todo_list_serializer = TodoListSerializer(data = request.data)

        if todo_list_serializer.is_valid():
            todo_list_serializer.save(author_ip = author_ip)
            return Response({'task_id': todo_list_serializer.data['id']})
        return Response(status = status.HTTP_400_BAD_REQUEST)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Class to modified if exist specified object if not return 404 status"""
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    name = 'tododetail'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        self.update(request, *args, **kwargs)
        return Response(status = status.HTTP_204_NO_CONTENT)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'todolist': reverse(TodoListView.name, request = request)
        })
