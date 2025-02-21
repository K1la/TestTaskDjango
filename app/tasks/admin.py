from django.contrib import admin
from .models import Task


# регистрируем Task в админ панеле
admin.site.register(Task)