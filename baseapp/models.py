from hashlib import blake2b
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    User =  models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank = True)
    Title = models.CharField(max_length=200, null= True, blank= True)
    description = models.TextField(null= True, blank= False, default= 'Escreva sua tarefa aqui!')
    task_done = models.BooleanField(default= False)
    date_of_create = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.Title

    

    class Meta:
        ordering = ['task_done']
        verbose_name = 'Tarefa'
