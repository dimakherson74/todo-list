from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo_app.models import Task


class TaskListView(ListView):
    model = Task



class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:todo-list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:todo-list")


class TaskDeleteView(DeleteView):
    model = Task
