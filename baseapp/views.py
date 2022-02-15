from dataclasses import field
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Tasks
from .urls import *

class TasklistView(ListView):
    model = Tasks
    context_object_name = 'Tasks'





class Details(DetailView):
    model  = Tasks
    context_object_name = 'Details of Task'
    template_name = 'baseapp/tasks_detail.html'



class Taskcreatingviews(CreateView):
    def get_success_url(self):
        return reverse('tasks_list')

    model = Tasks
    fields = '__all__'


class TasksUp(UpdateView):
    def get_success_url(self):
        return reverse('tasks_list')
    
    model = Tasks
    fields = '__all__'

class TasksDelete(DeleteView):
    def get_success_url(self):
        return reverse('tasks_list')

    model = Tasks
    fields = '__all__'


    