from django.shortcuts import render
from .models import Task
from django.utils import timezone
def home(request):
    tasks = []
    tasks = Task.objects.all()
    count = tasks.count
    for t in tasks:
        if t.DueDate < timezone.now():
            t.delete() 
    return render(request, 'todo/index.html', {'tasks':tasks, 'count':count})
