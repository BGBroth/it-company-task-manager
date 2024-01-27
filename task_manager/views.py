from django.shortcuts import render

from task_manager.models import Worker, Task


def index(request):
    """View function for the home page of the site."""

    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }

    return render(request, "task_manager/index.html", context=context)
