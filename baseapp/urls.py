from django.urls import path
from  . import views
from baseapp.templates.baseapp import *
from baseapp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('', views.TasklistView.as_view(), name = 'tasks_list'),
    path ('tasksdetails/<int:pk>', views.Details.as_view(), name = 'tasks_detail'),
    path ('createtask', views.Taskcreatingviews.as_view(), name = 'tasks_form'),
    path ('edit/<int:pk>', views.TasksUp.as_view(), name = 'tasks_edit'),
    path ('delete/<int:pk>', views.TasksDelete.as_view(), name = 'tasks_delete'),
    path ('login', views.loginlogout.as_view(), name  = 'loginFunc'),
    path ('logout', LogoutView.as_view(next_page = 'loginFunc'), name  = 'logoutFunc'),
    path ('createuser', views.RegisterUser.as_view(), name = 'RegisterPage')
]