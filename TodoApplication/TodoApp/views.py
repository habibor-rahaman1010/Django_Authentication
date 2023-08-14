from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.

class Todos(ListView):
    template_name = './index.html'
    model = models.Task
    context_object_name = 'items'

class AddTodoForm(FormView):
    template_name = './add_todo.html'
    form_class = forms.TodoForm
    model = models.Task
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

class TodoUpdate(UpdateView):
    form_class = forms.TodoForm
    template_name = './add_todo.html'
    model = models.Task
    success_url = reverse_lazy('home')

class DeleteTodo(DeleteView):
    model = models.Task
    template_name = './delete_confirm.html'
    success_url = reverse_lazy('home')

class FinishTodo(DeleteView):
    model = models.Task
    template_name = './done.html'
    success_url = reverse_lazy('home')

class CompleteTask(ListView):
    template_name = './completeTask.html'
    model = models.Task
    context_object_name = 'items'

    def get_queryset(self):
        return self.model.objects.filter(status=True)
    
class UnCompleteTask(ListView):
    template_name = './uncompleteTask.html'
    model = models.Task
    context_object_name = 'items'

    def get_queryset(self):
        return self.model.objects.filter(status=False)

class CompleteTaskView(View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs['pk']
        task = models.Task.objects.get(pk=task_id)
        task.status = True
        task.save()
        return HttpResponseRedirect(reverse('home'))
        # return redirect('home')