from django.contrib import admin
from .models import TaskType, Position, Worker, Task


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'position')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'deadline', 'is_completed', 'priority', 'task_type')
    filter_horizontal = ('assignees',)
