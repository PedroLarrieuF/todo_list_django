from select import select
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from .models import Tasks
from .urls import *


class TasklistView(LoginRequiredMixin,ListView):
    model = Tasks
    context_object_name = 'Tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['Tasks'] = context['Tasks'].filter(User = self.request.user)
        context['Count'] = context['Tasks'].filter(task_done = False).count()
        context['DoneTasks'] = context['Tasks'].filter(task_done = True).count()


        return context


class Details(LoginRequiredMixin,DetailView):
    model  = Tasks
    context_object_name = 'task'
    template_name = 'baseapp/tasks_detail.html'



class Taskcreatingviews(LoginRequiredMixin,CreateView):
    def get_success_url(self):
        return reverse('tasks_list')

    model = Tasks
    fields = '__all__'



class TasksUp(LoginRequiredMixin,UpdateView):
    def get_success_url(self):
        return reverse('tasks_list')
    
    model = Tasks
    fields = '__all__'

class TasksDelete(LoginRequiredMixin,DeleteView):
    def get_success_url(self):
        return reverse('tasks_list')

    model = Tasks
    fields = '__all__'


class loginlogout (LoginView):
    template_name = 'baseapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('tasks_list')

class RegisterUser(FormView):
    template_name = 'baseapp/createuser.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse('tasks_list')
