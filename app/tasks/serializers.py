from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # работаем с моделью Task
        model = Task
        # работаем с полями из модели Task и возвращаем клиенту эти поля
        fields = ['id', 'title', 'description', 'time_create', 'status']
        read_only_fields = ['time_create']