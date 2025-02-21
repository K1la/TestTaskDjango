from rest_framework import viewsets, generics, filters
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend


# в viewsets реализуются GET POST DELETE PUT запросы,
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    # фильтр по статусу задачи
    filterset_fields = ['status']



# ListCreateAPIview - реализует GET и POST - запросы
# class TaskAPIList(generics.ListCreateAPIView):
#     # список записей возвращаемых клиенту
#     queryset = Task.objects.all()
#     # сериализатор, который мы будем применять queryset
#     serializer_class = TaskSerializer
#
# # UpdateAPIView - реализация UPDATE(PUT) запросов
# class TaskAPIUpdate(generics.UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# # GET PUT DELETE - запросы
# class TaskAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

