from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView, CreateView, UpdateView
from . models import Task
from .forms import TaskForm, EditTaskForm


class TaskView(ListView):
    model = Task
    template_name = 'tasks.html'

    # Список начинается с последнего
    ordering = ['-date_created']


def category_view(request, category_name):
    category_task = Task.objects.filter(
        category=category_name).order_by('-date_created')
    return render(request, 'category.html', {'category_name': category_name, 'category_task': category_task})


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'index.html'
    # fields = '__all__'
    # fields = ('category', 'department', 'initiator', 'phone_number', 'description',)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.department = self.request.user
        self.object.save()
        return super(AddTaskView, self).form_valid(form)


class UpdateTaskView(UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'update_task.html'
    #fields = ['performer', 'completed', 'date_completed']
