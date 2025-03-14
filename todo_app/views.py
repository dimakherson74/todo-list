from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo_app.models import Task, Tag


class TaskListView(ListView):
    model = Task



class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:task-list")


class TagListView(ListView):
    model = Tag



class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = True
    task.save()
    return redirect("todo_app:task-list")


def undo_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = False
    task.save()
    return redirect("todo_app:task-list")
