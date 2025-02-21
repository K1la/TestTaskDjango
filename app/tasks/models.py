from django.db import models

# Создание полей для модели "Задачи"
class Task(models.Model):
    # Список статусов выполнения задач
    STATUS_CHOICES = [
        # в ожидании выполнения
        ('pending', 'Pending'),
        # в процессе выполнения
        ('in_progress', 'In Progress'),
        # выполнен
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание задачи", blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус выполнения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"